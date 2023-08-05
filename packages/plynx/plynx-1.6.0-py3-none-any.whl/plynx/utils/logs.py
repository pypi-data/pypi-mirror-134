import logging


def set_logging_level(verbose):
    levels = {
        0: logging.CRITICAL,
        1: logging.ERROR,
        2: logging.WARNING,
        3: logging.INFO,
        4: logging.DEBUG
    }
    root = logging.getLogger()
    root.setLevel(levels.get(verbose, logging.DEBUG))
