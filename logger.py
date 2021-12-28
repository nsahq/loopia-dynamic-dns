#!/usr/bin/python3
"""
Log manager for easy and fast log compliancy

This library is for educational purposes only.
Do no evil, do not break local or internation laws!
By using this code, you take full responisbillity for your actions.
The author have granted code access for educational purposes and is
not liable for any missuse.
"""
__author__ = "Jonas Werme"
__copyright__ = "Copyright (c) 2021 Jonas Werme"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Jonas Werme"
__email__ = "jonas[dot]werme[at]hoofbite[dot]com"
__status__ = "Prototype"

import inspect
import logging


def get_logger(
    name: str = "",
    log_level_console: int = logging.DEBUG,
    log_level_file: int = logging.DEBUG,
    log_file: str = "application.log",
) -> logging.Logger:
    """
    Creates and returns a logger instance as per hoofbite style guides.

    Turn off console or file logging by setting the corresponding log level to 0.

    Arguments:
        name {string} -- Logger name. Defaults to calling modules __name__ property.
        log_level_console {int} -- Log level for console logging. 0-50 in increments by 10. Defaults to 20 (logging.INFO).
        log_level_file {int} -- Log level for file logging. 0-50 in increments by 10. Defaults to 20 (logging.INFO).
        log_file {string} -- Path to log file. Defaults to application.log.

    Returns:
        logging.Logger -- Logger with handler(s) as defined by parameters
    """

    # Set formatting rules
    cfmt = logging.Formatter("[%(levelname)s] %(message)s")
    ffmt = logging.Formatter("%(asctime)-15s [%(levelname)s] %(message)s")

    logging.root.setLevel(logging.NOTSET)

    # Set calling modules name if none was supplied
    if name == "":
        frm = inspect.stack()[1]
        mod = inspect.getmodule(frm[0])
        name = mod.__name__

    log = logging.getLogger(name)

    # Console logging
    if log_level_console != 0:
        ch = logging.StreamHandler()
        ch.setLevel(log_level_console)
        ch.setFormatter(cfmt)
        log.addHandler(ch)

    # File logging
    if log_file != "" and log_level_file != 0:
        fh = logging.FileHandler(log_file)
        fh.setLevel(log_level_file)
        fh.setFormatter(ffmt)
        log.addHandler(fh)

    return log


def get_logger_from_dict(cfg):
    pass
