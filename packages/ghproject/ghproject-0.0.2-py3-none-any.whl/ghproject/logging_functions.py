"""
---
Adapted from https://github.com/matchms/matchms/blob/master/matchms/logging_functions.py
Licensed under Apache License, version 2.0
Copyright (c) 2021, Netherlands eScience Center
---

ghproject functions and method report unexpected or undesired behavior as
logging WARNING, and additional information as INFO.
The default logging level is set to WARNING. If you want to output additional
logging messages, you can lower the logging level to INFO using set_logger_level:

.. code-block:: python
    from ghproject import set_logger_level
    set_logger_level("INFO")

If you want to suppress logging warnings, you can also raise the logging level
to ERROR by:

.. code-block:: python
    set_logger_level("ERROR")

To write logging entries to a local file, you can do the following:

.. code-block:: python
    from ghproject.logging_functions import add_logging_to_file
    add_logging_to_file("sample.log", loglevel="INFO")

If you want to write the logging messages to a local file while silencing the
stream of such messages, you can do the following:

.. code-block:: python
    from ghproject.logging_functions import add_logging_to_file
    add_logging_to_file("sample.log", loglevel="INFO",
                        remove_stream_handlers=True)

"""

import logging
import logging.config
import sys


_formatter = logging.Formatter(
    "%(asctime)s : %(levelname)s : [%(module)s:%(funcName)s] : %(message)s"
)


def init_logger(logger_name="ghproject"):
    """Initialize ghproject logger.

    Parameters
    ----------
    logger_name : str
        name of the logger, default is ghproject

    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.WARNING)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.WARNING)
    handler.setFormatter(_formatter)
    logger.addHandler(handler)
    logger.info("Completed configuring ghproject logger.")


def set_logger_level(loglevel: str, logger_name="ghproject"):
    """Update logging level to given loglevel.

    Parameters
    ----------
    loglevels
        Can be 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.
    logger_name
        Default is "ghproject". Change if logger name should be different.
    """
    level = logging.getLevelName(loglevel)
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    for handler in logger.handlers:
        handler.setLevel(level)


def add_logging_to_file(
    filename: str,
    loglevel: str = "INFO",
    remove_stream_handlers: bool = False,
    logger_name="ghproject",
):
    """Add logging to file.
    Current implementation does not change the initial logging stream,
    but simply adds a FileHandler to write logging entries to a file.
    Parameters
    ----------
    filename
        Name of file for write logging output.
    loglevels
        Can be 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'.
    remove_stream_handlers
        Set to True if only logging to file is desired.
    logger_name
        Default is "ghproject". Change if logger name should be different.
    """
    level = logging.getLevelName(loglevel)
    logger = logging.getLogger(logger_name)
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(level)
    file_handler.setFormatter(_formatter)
    logger.addHandler(file_handler)

    # Remove the existing handlers if they are not of type FileHandler
    if remove_stream_handlers is True:
        for handler in logger.handlers:
            if not isinstance(handler, logging.FileHandler):
                logger.removeHandler(handler)


def reset_logger(logger_name="ghproject"):
    """Reset ghproject logger to initial state.
    This will remove all logging Handlers and initialize a new ghproject logger.
    Use this function to reset previous changes made to the default ghproject logger.
    Parameters
    ----------
    logger_name
        Default is "ghproject". Change if logger name should be different.
    """
    logger = logging.getLogger(logger_name)
    logger.handlers.clear()
    init_logger()
