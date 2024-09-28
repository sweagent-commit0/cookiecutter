"""Module for setting up logging."""
import logging
import sys
LOG_LEVELS = {'DEBUG': logging.DEBUG, 'INFO': logging.INFO, 'WARNING': logging.WARNING, 'ERROR': logging.ERROR, 'CRITICAL': logging.CRITICAL}
LOG_FORMATS = {'DEBUG': '%(levelname)s %(name)s: %(message)s', 'INFO': '%(levelname)s: %(message)s'}

def configure_logger(stream_level='DEBUG', debug_file=None):
    """Configure logging for cookiecutter.

    Set up logging to stdout with given level. If ``debug_file`` is given set
    up logging to file with DEBUG level.
    """
    pass