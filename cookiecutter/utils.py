"""Helper functions used throughout Cookiecutter."""
import contextlib
import logging
import os
import shutil
import stat
import tempfile
from pathlib import Path
from typing import Dict
from jinja2.ext import Extension
from cookiecutter.environment import StrictEnvironment
logger = logging.getLogger(__name__)

def force_delete(func, path, exc_info):
    """Error handler for `shutil.rmtree()` equivalent to `rm -rf`.

    Usage: `shutil.rmtree(path, onerror=force_delete)`
    From https://docs.python.org/3/library/shutil.html#rmtree-example
    """
    pass

def rmtree(path):
    """Remove a directory and all its contents. Like rm -rf on Unix.

    :param path: A directory path.
    """
    pass

def make_sure_path_exists(path: 'os.PathLike[str]') -> None:
    """Ensure that a directory exists.

    :param path: A directory tree path for creation.
    """
    pass

@contextlib.contextmanager
def work_in(dirname=None):
    """Context manager version of os.chdir.

    When exited, returns to the working directory prior to entering.
    """
    pass

def make_executable(script_path):
    """Make `script_path` executable.

    :param script_path: The file to change
    """
    pass

def simple_filter(filter_function):
    """Decorate a function to wrap it in a simplified jinja2 extension."""
    pass

def create_tmp_repo_dir(repo_dir: 'os.PathLike[str]') -> Path:
    """Create a temporary dir with a copy of the contents of repo_dir."""
    pass

def create_env_with_context(context: Dict):
    """Create a jinja environment using the provided context."""
    pass