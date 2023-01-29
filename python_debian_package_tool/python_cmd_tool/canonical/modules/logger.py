""" Defining the Logger """

import logging
import os
from logging import Logger


def def_logger(log_dir: str) -> Logger:
    """
    Define & Configure the Logger
    Args:
        log_dir: the directory for the log files
    Returns:
        root_logger: configured root logger
    """

    # define log file
    logfile_name = "log_info.log"
    logfile_path = os.path.join(log_dir, "logs", logfile_name)

    # create root logger & set log level
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # define handlers - file & stream handler
    fh = logging.FileHandler(logfile_path)
    fh.setLevel(logging.WARNING)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # define formatter
    formatter = logging.Formatter(
        "%(asctime)s  %(levelname)s  %(message)s [%(filename)s]"
    )

    # set formatter
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add handlers to logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
