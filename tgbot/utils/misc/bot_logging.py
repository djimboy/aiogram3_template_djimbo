# - *- coding: utf- 8 - *-
import logging


from colorlog import ColoredFormatter


# Build logging
def start_logging():
    log_formatter_file = logging.Formatter(u"[%(levelname)s] [%(asctime)s] | [%(filename)s LINE:%(lineno)d] | %(message)s")
    log_formatter_console = ColoredFormatter(
        "%(cyan)s%(asctime)s %(blue)s| %(log_color)s%(levelname)s %(blue)s"
        "| %(purple)s%(filename)s:%(lineno)d %(blue)s| %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
    )

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("logs.log", "w", "utf-8")
    file_handler.setFormatter(log_formatter_file)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter_console)
    console_handler.setLevel(logging.ERROR)

    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    return root_logger
