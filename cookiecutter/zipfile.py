"""Utility functions for handling and fetching repo archives in zip format."""
import os
import tempfile
from pathlib import Path
from typing import Optional
from zipfile import BadZipFile, ZipFile
import requests
from cookiecutter.exceptions import InvalidZipRepository
from cookiecutter.prompt import prompt_and_delete, read_repo_password
from cookiecutter.utils import make_sure_path_exists

def unzip(zip_uri: str, is_url: bool, clone_to_dir: 'os.PathLike[str]'='.', no_input: bool=False, password: Optional[str]=None):
    """Download and unpack a zipfile at a given URI.

    This will download the zipfile to the cookiecutter repository,
    and unpack into a temporary directory.

    :param zip_uri: The URI for the zipfile.
    :param is_url: Is the zip URI a URL or a file?
    :param clone_to_dir: The cookiecutter repository directory
        to put the archive into.
    :param no_input: Do not prompt for user input and eventually force a refresh of
        cached resources.
    :param password: The password to use when unpacking the repository.
    """
    pass