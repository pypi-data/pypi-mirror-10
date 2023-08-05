#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Commands, largely through subprocess.

Not wrapping subprocess.call() or subprocess.check_call() because they don't
support using subprocess.PIPE for stdout/stderr; redirecting stdout and stderr
assumes synchronous behavior.

This module is starting very small, but there are plans to add equivalents to
run_command() and get_output_from_command() from mozharness shortly.

Attributes:
  STRINGS (dict): Strings for logging.
"""
from __future__ import absolute_import, division, print_function, \
                       unicode_literals
import logging
import os
import subprocess

LOGGER_NAME = "scriptharness.commands"
STRINGS = {
    "check_output": {
        "pre_msg":
            "Running subprocess.check_output() with %(args)s %(kwargs)s",
    },
}


def makedirs(path, level=logging.INFO):
    """os.makedirs() wrapper.

    Args:
      path (str): path to the directory
      level (int, optional): the logging level to log with.
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.log(level, "Creating directory %s", path)
    if not os.path.exists(path):
        os.makedirs(path)
        logger.log(level, "Done.")
    else:
        logger.log(level, "Already exists.")

def make_parent_dir(path, **kwargs):
    """Create the parent of path if it doesn't exist.

    Args:
      path (str): path to the file.
      **kwargs: These are passed to makedirs().
    """
    dirname = os.path.dirname(path)
    if dirname:
        makedirs(dirname, **kwargs)

def check_output(command, logger_name="scriptharness.commands.check_output",
                 level=logging.INFO, log_output=True, **kwargs):
    """Wrap subprocess.check_output with logging

    Args:
      command (str or list): The command to run.
      logger_name (str, optional): the logger name to log with.
      level (int, optional): the logging level to log with.  Defaults to
        logging.INFO
      log_output (bool, optional): When true, log the output of the command.
        Defaults to True.
      **kwargs: sent to `subprocess.check_output()`
    """
    logger = logging.getLogger(logger_name)
    logger.log(level, STRINGS['check_output']['pre_msg'],
               {'args': (), 'kwargs': kwargs})
    output = subprocess.check_output(command, **kwargs)
    if log_output:
        logger = logging.getLogger(logger_name)
        logger.info("Output:")
        for line in output.splitlines():
            logger.log(level, " %s", line)
    return output
