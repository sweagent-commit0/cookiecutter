"""Global configuration handling."""
import collections
import copy
import logging
import os
import yaml
from cookiecutter.exceptions import ConfigDoesNotExistException, InvalidConfiguration
logger = logging.getLogger(__name__)
USER_CONFIG_PATH = os.path.expanduser('~/.cookiecutterrc')
BUILTIN_ABBREVIATIONS = {'gh': 'https://github.com/{0}.git', 'gl': 'https://gitlab.com/{0}.git', 'bb': 'https://bitbucket.org/{0}'}
DEFAULT_CONFIG = {'cookiecutters_dir': os.path.expanduser('~/.cookiecutters/'), 'replay_dir': os.path.expanduser('~/.cookiecutter_replay/'), 'default_context': collections.OrderedDict([]), 'abbreviations': BUILTIN_ABBREVIATIONS}

def _expand_path(path):
    """Expand both environment variables and user home in the given path."""
    pass

def merge_configs(default, overwrite):
    """Recursively update a dict with the key/value pair of another.

    Dict values that are dictionaries themselves will be updated, whilst
    preserving existing keys.
    """
    pass

def get_config(config_path):
    """Retrieve the config from the specified path, returning a config dict."""
    pass

def get_user_config(config_file=None, default_config=False):
    """Return the user config as a dict.

    If ``default_config`` is True, ignore ``config_file`` and return default
    values for the config parameters.

    If ``default_config`` is a dict, merge values with default values and return them
    for the config parameters.

    If a path to a ``config_file`` is given, that is different from the default
    location, load the user config from that.

    Otherwise look up the config file path in the ``COOKIECUTTER_CONFIG``
    environment variable. If set, load the config from this path. This will
    raise an error if the specified path is not valid.

    If the environment variable is not set, try the default config file path
    before falling back to the default config values.
    """
    pass