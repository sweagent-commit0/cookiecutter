"""
cookiecutter.replay.

-------------------
"""
import json
import os
from cookiecutter.utils import make_sure_path_exists

def get_file_name(replay_dir, template_name):
    """Get the name of file."""
    pass

def dump(replay_dir: 'os.PathLike[str]', template_name: str, context: dict):
    """Write json data to file."""
    pass

def load(replay_dir, template_name):
    """Read json data from file."""
    pass