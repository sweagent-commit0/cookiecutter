"""Functions for finding Cookiecutter templates and other components."""
import logging
import os
from pathlib import Path
from jinja2 import Environment
from cookiecutter.exceptions import NonTemplatedInputDirException
logger = logging.getLogger(__name__)

def find_template(repo_dir: 'os.PathLike[str]', env: Environment) -> Path:
    """Determine which child directory of ``repo_dir`` is the project template.

    :param repo_dir: Local directory of newly cloned repo.
    :return: Relative path to project template.
    """
    pass