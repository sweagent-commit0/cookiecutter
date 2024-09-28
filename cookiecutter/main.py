"""
Main entry point for the `cookiecutter` command.

The code in this module is also a good example of how to use Cookiecutter as a
library rather than a script.
"""
import logging
import os
import sys
from copy import copy
from pathlib import Path
from cookiecutter.config import get_user_config
from cookiecutter.exceptions import InvalidModeException
from cookiecutter.generate import generate_context, generate_files
from cookiecutter.hooks import run_pre_prompt_hook
from cookiecutter.prompt import choose_nested_template, prompt_for_config
from cookiecutter.replay import dump, load
from cookiecutter.repository import determine_repo_dir
from cookiecutter.utils import rmtree
logger = logging.getLogger(__name__)

def cookiecutter(template, checkout=None, no_input=False, extra_context=None, replay=None, overwrite_if_exists=False, output_dir='.', config_file=None, default_config=False, password=None, directory=None, skip_if_file_exists=False, accept_hooks=True, keep_project_on_failure=False):
    """
    Run Cookiecutter just as if using it from the command line.

    :param template: A directory containing a project template directory,
        or a URL to a git repository.
    :param checkout: The branch, tag or commit ID to checkout after clone.
    :param no_input: Do not prompt for user input.
        Use default values for template parameters taken from `cookiecutter.json`, user
        config and `extra_dict`. Force a refresh of cached resources.
    :param extra_context: A dictionary of context that overrides default
        and user configuration.
    :param replay: Do not prompt for input, instead read from saved json. If
        ``True`` read from the ``replay_dir``.
        if it exists
    :param overwrite_if_exists: Overwrite the contents of the output directory
        if it exists.
    :param output_dir: Where to output the generated project dir into.
    :param config_file: User configuration file path.
    :param default_config: Use default values rather than a config file.
    :param password: The password to use when extracting the repository.
    :param directory: Relative path to a cookiecutter template in a repository.
    :param skip_if_file_exists: Skip the files in the corresponding directories
        if they already exist.
    :param accept_hooks: Accept pre and post hooks if set to `True`.
    :param keep_project_on_failure: If `True` keep generated project directory even when
        generation fails
    """
    pass

class _patch_import_path_for_repo:

    def __init__(self, repo_dir: 'os.PathLike[str]'):
        self._repo_dir = f'{repo_dir}' if isinstance(repo_dir, Path) else repo_dir
        self._path = None

    def __enter__(self):
        self._path = copy(sys.path)
        sys.path.append(self._repo_dir)

    def __exit__(self, type, value, traceback):
        sys.path = self._path