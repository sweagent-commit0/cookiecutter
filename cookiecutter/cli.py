"""Main `cookiecutter` CLI."""
import collections
import json
import os
import sys
import click
from cookiecutter import __version__
from cookiecutter.config import get_user_config
from cookiecutter.exceptions import ContextDecodingException, FailedHookException, InvalidModeException, InvalidZipRepository, OutputDirExistsException, RepositoryCloneFailed, RepositoryNotFound, UndefinedVariableInTemplate, UnknownExtension
from cookiecutter.log import configure_logger
from cookiecutter.main import cookiecutter

def version_msg():
    """Return the Cookiecutter version, location and Python powering it."""
    pass

def validate_extra_context(ctx, param, value):
    """Validate extra context."""
    pass

def list_installed_templates(default_config, passed_config_file):
    """List installed (locally cloned) templates. Use cookiecutter --list-installed."""
    pass

@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(__version__, '-V', '--version', message=version_msg())
@click.argument('template', required=False)
@click.argument('extra_context', nargs=-1, callback=validate_extra_context)
@click.option('--no-input', is_flag=True, help='Do not prompt for parameters and only use cookiecutter.json file content. Defaults to deleting any cached resources and redownloading them. Cannot be combined with the --replay flag.')
@click.option('-c', '--checkout', help='branch, tag or commit to checkout after git clone')
@click.option('--directory', help='Directory within repo that holds cookiecutter.json file for advanced repositories with multi templates in it')
@click.option('-v', '--verbose', is_flag=True, help='Print debug information', default=False)
@click.option('--replay', is_flag=True, help='Do not prompt for parameters and only use information entered previously. Cannot be combined with the --no-input flag or with extra configuration passed.')
@click.option('--replay-file', type=click.Path(), default=None, help='Use this file for replay instead of the default.')
@click.option('-f', '--overwrite-if-exists', is_flag=True, help='Overwrite the contents of the output directory if it already exists')
@click.option('-s', '--skip-if-file-exists', is_flag=True, help='Skip the files in the corresponding directories if they already exist', default=False)
@click.option('-o', '--output-dir', default='.', type=click.Path(), help='Where to output the generated project dir into')
@click.option('--config-file', type=click.Path(), default=None, help='User configuration file')
@click.option('--default-config', is_flag=True, help='Do not load a config file. Use the defaults instead')
@click.option('--debug-file', type=click.Path(), default=None, help='File to be used as a stream for DEBUG logging')
@click.option('--accept-hooks', type=click.Choice(['yes', 'ask', 'no']), default='yes', help='Accept pre/post hooks')
@click.option('-l', '--list-installed', is_flag=True, help='List currently installed templates.')
@click.option('--keep-project-on-failure', is_flag=True, help='Do not delete project folder on failure')
def main(template, extra_context, no_input, checkout, verbose, replay, overwrite_if_exists, output_dir, config_file, default_config, debug_file, directory, skip_if_file_exists, accept_hooks, replay_file, list_installed, keep_project_on_failure):
    """Create a project from a Cookiecutter project template (TEMPLATE).

    Cookiecutter is free and open source software, developed and managed by
    volunteers. If you would like to help out or fund the project, please get
    in touch at https://github.com/cookiecutter/cookiecutter.
    """
    pass
if __name__ == '__main__':
    main()