import logging
from logging.handlers import RotatingFileHandler
from config import Config
from os.path import join


def set_logger(logger=logging.getLogger()):
    # Ser level
    logger.setLevel(logging.DEBUG)

    # Create handlers
    info_handler = logging.handlers.RotatingFileHandler(
        filename=join(Config.LOGDIR, "info.log"),
        maxBytes=10485760,  # 1 MB
        backupCount=1,
    )

    info_handler.setLevel(logging.INFO)
    error_handler = logging.handlers.RotatingFileHandler(
        filename=join(Config.LOGDIR, "error.log"),
        maxBytes=10485760,  # 1 MB
        backupCount=1,
    )
    error_handler.setLevel(logging.ERROR)

    # Create formatter
    detailed_formatter = logging.Formatter(
        fmt="%(levelname)s %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n"
    )

    # Hook it all up
    info_handler.setFormatter(fmt=detailed_formatter)
    error_handler.setFormatter(fmt=detailed_formatter)
    logger.addHandler(hdlr=info_handler)
    logger.addHandler(hdlr=error_handler)
