"""Functions for prompting the user for project info."""
import json
import os
import re
import sys
from collections import OrderedDict
from pathlib import Path
from jinja2.exceptions import UndefinedError
from rich.prompt import Confirm, InvalidResponse, Prompt, PromptBase
from cookiecutter.exceptions import UndefinedVariableInTemplate
from cookiecutter.utils import create_env_with_context, rmtree

def read_user_variable(var_name, default_value, prompts=None, prefix=''):
    """Prompt user for variable and return the entered value or given default.

    :param str var_name: Variable of the context to query the user
    :param default_value: Value that will be returned if no input happens
    """
    pass

class YesNoPrompt(Confirm):
    """A prompt that returns a boolean for yes/no questions."""
    yes_choices = ['1', 'true', 't', 'yes', 'y', 'on']
    no_choices = ['0', 'false', 'f', 'no', 'n', 'off']

    def process_response(self, value: str) -> bool:
        """Convert choices to a bool."""
        pass

def read_user_yes_no(var_name, default_value, prompts=None, prefix=''):
    """Prompt the user to reply with 'yes' or 'no' (or equivalent values).

    - These input values will be converted to ``True``:
      "1", "true", "t", "yes", "y", "on"
    - These input values will be converted to ``False``:
      "0", "false", "f", "no", "n", "off"

    Actual parsing done by :func:`prompt`; Check this function codebase change in
    case of unexpected behaviour.

    :param str question: Question to the user
    :param default_value: Value that will be returned if no input happens
    """
    pass

def read_repo_password(question):
    """Prompt the user to enter a password.

    :param str question: Question to the user
    """
    pass

def read_user_choice(var_name, options, prompts=None, prefix=''):
    """Prompt the user to choose from several options for the given variable.

    The first item will be returned if no input happens.

    :param str var_name: Variable as specified in the context
    :param list options: Sequence of options that are available to select from
    :return: Exactly one item of ``options`` that has been chosen by the user
    """
    pass
DEFAULT_DISPLAY = 'default'

def process_json(user_value, default_value=None):
    """Load user-supplied value as a JSON dict.

    :param str user_value: User-supplied value to load as a JSON dict
    """
    pass

class JsonPrompt(PromptBase[dict]):
    """A prompt that returns a dict from JSON string."""
    default = None
    response_type = dict
    validate_error_message = '[prompt.invalid]  Please enter a valid JSON string'

    def process_response(self, value: str) -> dict:
        """Convert choices to a dict."""
        pass

def read_user_dict(var_name, default_value, prompts=None, prefix=''):
    """Prompt the user to provide a dictionary of data.

    :param str var_name: Variable as specified in the context
    :param default_value: Value that will be returned if no input is provided
    :return: A Python dictionary to use in the context.
    """
    pass

def render_variable(env, raw, cookiecutter_dict):
    """Render the next variable to be displayed in the user prompt.

    Inside the prompting taken from the cookiecutter.json file, this renders
    the next variable. For example, if a project_name is "Peanut Butter
    Cookie", the repo_name could be be rendered with:

        `{{ cookiecutter.project_name.replace(" ", "_") }}`.

    This is then presented to the user as the default.

    :param Environment env: A Jinja2 Environment object.
    :param raw: The next value to be prompted for by the user.
    :param dict cookiecutter_dict: The current context as it's gradually
        being populated with variables.
    :return: The rendered value for the default variable.
    """
    pass

def _prompts_from_options(options: dict) -> dict:
    """Process template options and return friendly prompt information."""
    pass

def prompt_choice_for_template(key, options, no_input):
    """Prompt user with a set of options to choose from.

    :param no_input: Do not prompt for user input and return the first available option.
    """
    pass

def prompt_choice_for_config(cookiecutter_dict, env, key, options, no_input, prompts=None, prefix=''):
    """Prompt user with a set of options to choose from.

    :param no_input: Do not prompt for user input and return the first available option.
    """
    pass

def prompt_for_config(context, no_input=False):
    """Prompt user to enter a new config.

    :param dict context: Source for field names and sample values.
    :param no_input: Do not prompt for user input and use only values from context.
    """
    pass

def choose_nested_template(context: dict, repo_dir: str, no_input: bool=False) -> str:
    """Prompt user to select the nested template to use.

    :param context: Source for field names and sample values.
    :param repo_dir: Repository directory.
    :param no_input: Do not prompt for user input and use only values from context.
    :returns: Path to the selected template.
    """
    pass

def prompt_and_delete(path, no_input=False):
    """
    Ask user if it's okay to delete the previously-downloaded file/directory.

    If yes, delete it. If no, checks to see if the old version should be
    reused. If yes, it's reused; otherwise, Cookiecutter exits.

    :param path: Previously downloaded zipfile.
    :param no_input: Suppress prompt to delete repo and just delete it.
    :return: True if the content was deleted
    """
    pass