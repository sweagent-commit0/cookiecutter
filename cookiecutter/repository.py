"""Cookiecutter repository functions."""
import os
import re
from cookiecutter.exceptions import RepositoryNotFound
from cookiecutter.vcs import clone
from cookiecutter.zipfile import unzip
REPO_REGEX = re.compile('\n# something like git:// ssh:// file:// etc.\n((((git|hg)\\+)?(git|ssh|file|https?):(//)?)\n |                                      # or\n (\\w+@[\\w\\.]+)                          # something like user@...\n)\n', re.VERBOSE)

def is_repo_url(value):
    """Return True if value is a repository URL."""
    pass

def is_zip_file(value):
    """Return True if value is a zip file."""
    pass

def expand_abbreviations(template, abbreviations):
    """Expand abbreviations in a template name.

    :param template: The project template name.
    :param abbreviations: Abbreviation definitions.
    """
    pass

def repository_has_cookiecutter_json(repo_directory):
    """Determine if `repo_directory` contains a `cookiecutter.json` file.

    :param repo_directory: The candidate repository directory.
    :return: True if the `repo_directory` is valid, else False.
    """
    pass

def determine_repo_dir(template, abbreviations, clone_to_dir, checkout, no_input, password=None, directory=None):
    """
    Locate the repository directory from a template reference.

    Applies repository abbreviations to the template reference.
    If the template refers to a repository URL, clone it.
    If the template is a path to a local repository, use it.

    :param template: A directory containing a project template directory,
        or a URL to a git repository.
    :param abbreviations: A dictionary of repository abbreviation
        definitions.
    :param clone_to_dir: The directory to clone the repository into.
    :param checkout: The branch, tag or commit ID to checkout after clone.
    :param no_input: Do not prompt for user input and eventually force a refresh of
        cached resources.
    :param password: The password to use when extracting the repository.
    :param directory: Directory within repo where cookiecutter.json lives.
    :return: A tuple containing the cookiecutter template directory, and
        a boolean describing whether that directory should be cleaned up
        after the template has been instantiated.
    :raises: `RepositoryNotFound` if a repository directory could not be found.
    """
    pass