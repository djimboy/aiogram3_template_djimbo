# - *- coding: utf- 8 - *-
import logging


# Build logging
def start_logging():
    log_formatter = logging.Formatter(u"[%(levelname)s] [%(asctime)s] | [%(filename)s LINE:%(lineno)d] | %(message)s")

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("logs.log", "w", "utf-8")
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    console_handler.setLevel(logging.ERROR)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    return root_logger
