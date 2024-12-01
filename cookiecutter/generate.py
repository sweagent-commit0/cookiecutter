"""Functions for generating a project from a project template."""
import fnmatch
import json
import logging
import os
import shutil
import warnings
from collections import OrderedDict
from pathlib import Path
from binaryornot.check import is_binary
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateSyntaxError, UndefinedError
from cookiecutter.exceptions import ContextDecodingException, OutputDirExistsException, UndefinedVariableInTemplate
from cookiecutter.find import find_template
from cookiecutter.hooks import run_hook_from_repo_dir
from cookiecutter.utils import create_env_with_context, make_sure_path_exists, rmtree, work_in
logger = logging.getLogger(__name__)

def is_copy_only_path(path, context):
    """Check whether the given `path` should only be copied and not rendered.

    Returns True if `path` matches a pattern in the given `context` dict,
    otherwise False.

    :param path: A file-system path referring to a file or dir that
        should be rendered or just copied.
    :param context: cookiecutter context.
    """
    copy_without_render = context.get("_copy_without_render", [])
    for pattern in copy_without_render:
        if fnmatch.fnmatch(path, pattern):
            return True
    return False

def apply_overwrites_to_context(context, overwrite_context, *, in_dictionary_variable=False):
    """Modify the given context in place based on the overwrite_context."""
    for key, value in overwrite_context.items():
        if isinstance(value, dict):
            if key not in context:
                context[key] = {}
            apply_overwrites_to_context(context[key], value, in_dictionary_variable=True)
        elif isinstance(value, list):
            if key not in context:
                context[key] = []
            context[key].extend(value)
        else:
            if in_dictionary_variable and key not in context:
                context[key] = value
            elif not in_dictionary_variable:
                context[key] = value

def generate_context(context_file='cookiecutter.json', default_context=None, extra_context=None):
    """Generate the context for a Cookiecutter project template.

    Loads the JSON file as a Python object, with key being the JSON filename.

    :param context_file: JSON file containing key/value pairs for populating
        the cookiecutter's variables.
    :param default_context: Dictionary containing config to take into account.
    :param extra_context: Dictionary containing configuration overrides
    """
    context = {}
    try:
        with open(context_file, 'r') as file:
            context = json.load(file, object_pairs_hook=OrderedDict)
    except ValueError as e:
        raise ContextDecodingException(context_file, str(e))

    # Apply default context
    if default_context:
        apply_overwrites_to_context(context, default_context)

    # Apply extra context
    if extra_context:
        apply_overwrites_to_context(context, extra_context)

    return context

def generate_file(project_dir, infile, context, env, skip_if_file_exists=False):
    """Render filename of infile as name of outfile, handle infile correctly.

    Dealing with infile appropriately:

        a. If infile is a binary file, copy it over without rendering.
        b. If infile is a text file, render its contents and write the
           rendered infile to outfile.

    Precondition:

        When calling `generate_file()`, the root template dir must be the
        current working directory. Using `utils.work_in()` is the recommended
        way to perform this directory change.

    :param project_dir: Absolute path to the resulting generated project.
    :param infile: Input file to generate the file from. Relative to the root
        template dir.
    :param context: Dict for populating the cookiecutter's variables.
    :param env: Jinja2 template execution environment.
    """
    logger.debug('Generating file %s', infile)

    # Render the path to the output file (not including the root project dir)
    outfile_tmpl = env.from_string(infile)
    outfile = outfile_tmpl.render(**context)
    outfile_path = os.path.join(project_dir, outfile)

    # Create the directories to the outfile if they don't exist
    dirname = os.path.dirname(outfile_path)
    make_sure_path_exists(dirname)

    if skip_if_file_exists and os.path.exists(outfile_path):
        logger.debug('File %s already exists, skipping', outfile)
        return

    # Just copy over binary files without rendering
    if is_binary(infile):
        shutil.copyfile(infile, outfile_path)
    else:
        # Force fwd slashes on Windows for jinja template
        infile_fwd_slashes = infile.replace(os.path.sep, '/')

        # Render the file
        try:
            tmpl = env.get_template(infile_fwd_slashes)
            rendered_file = tmpl.render(**context)
        except UndefinedError as err:
            msg = "Unable to create file '{}'".format(outfile)
            raise UndefinedVariableInTemplate(msg, err, context)
        except TemplateSyntaxError as err:
            msg = "Unable to create file '{}'".format(outfile)
            raise TemplateSyntaxError(msg, err.lineno, err.name, err.filename)

        # Write the file
        with open(outfile_path, 'w') as fh:
            fh.write(rendered_file)

    # Apply file permissions to output file
    shutil.copymode(infile, outfile_path)

def render_and_create_dir(dirname: str, context: dict, output_dir: 'os.PathLike[str]', environment: Environment, overwrite_if_exists: bool=False):
    """Render name of a directory, create the directory, return its path."""
    pass

def _run_hook_from_repo_dir(repo_dir, hook_name, project_dir, context, delete_project_on_failure):
    """Run hook from repo directory, clean project directory if hook fails.

    :param repo_dir: Project template input directory.
    :param hook_name: The hook to execute.
    :param project_dir: The directory to execute the script from.
    :param context: Cookiecutter project context.
    :param delete_project_on_failure: Delete the project directory on hook
        failure?
    """
    pass

def generate_files(repo_dir, context=None, output_dir='.', overwrite_if_exists=False, skip_if_file_exists=False, accept_hooks=True, keep_project_on_failure=False):
    """Render the templates and saves them to files.

    :param repo_dir: Project template input directory.
    :param context: Dict for populating the template's variables.
    :param output_dir: Where to output the generated project dir into.
    :param overwrite_if_exists: Overwrite the contents of the output directory
        if it exists.
    :param skip_if_file_exists: Skip the files in the corresponding directories
        if they already exist
    :param accept_hooks: Accept pre and post hooks if set to `True`.
    :param keep_project_on_failure: If `True` keep generated project directory even when
        generation fails
    """
    template_dir = find_template(repo_dir)
    logger.debug('Generating project from %s...', template_dir)
    context = context or {}

    unrendered_dir = os.path.split(template_dir)[1]
    env = create_env_with_context(context)
    project_dir = render_and_create_dir(unrendered_dir, context, output_dir, env, overwrite_if_exists)

    # We want the Jinja path and the OS paths to match. Consequently, we'll:
    #   + CD to the template folder
    #   + Walk the path and generate the files
    #   + CD back to where we started
    with work_in(template_dir):
        for root, dirs, files in os.walk('.'):
            for d in dirs:
                unrendered_dir = os.path.join(project_dir, root, d)
                render_and_create_dir(unrendered_dir, context, output_dir, env, overwrite_if_exists)

            for f in files:
                infile = os.path.join(root, f)
                if is_copy_only_path(infile, context):
                    outfile_path = os.path.join(project_dir, infile)
                    logger.debug('Copying %s to %s without rendering', infile, outfile_path)
                    shutil.copyfile(infile, outfile_path)
                    shutil.copymode(infile, outfile_path)
                    continue
                try:
                    generate_file(project_dir, infile, context, env, skip_if_file_exists)
                except UndefinedVariableInTemplate as err:
                    if not keep_project_on_failure:
                        rmtree(project_dir)
                    raise

    if accept_hooks:
        _run_hook_from_repo_dir(repo_dir, 'post_gen_project', project_dir, context, delete_project_on_failure=not keep_project_on_failure)

    return project_dir
