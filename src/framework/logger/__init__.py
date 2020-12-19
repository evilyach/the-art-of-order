import inspect
import logging
import os

import colorlog


class Logger:
    def __init__(self, level=logging.DEBUG):
        self.level = level
        self.handler = colorlog.StreamHandler()

        self.terminal_format = "%(asctime)s: %(log_color)s%(message)s%(reset)s"
        self.file_format = "%(asctime)s: %(message)s"
        self.datefmt = "%H:%M:%S %d/%m"
        self.log_colors = {
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        }

        self.terminal_formatter = colorlog.ColoredFormatter(
            self.terminal_format, datefmt=self.datefmt, log_colors=self.log_colors
        )
        self.file_formatter = logging.Formatter(
            self.file_format,
            datefmt=self.datefmt,
        )

        self.terminal_handler = logging.StreamHandler()
        self.terminal_handler.setLevel(self.level)
        self.terminal_handler.setFormatter(self.terminal_formatter)

        self.file_handler = logging.FileHandler("logs.txt")
        self.file_handler.setLevel(self.level)
        self.file_handler.setFormatter(self.file_formatter)

        self.logger = logging.getLogger("root")
        self.logger.setLevel(self.level)
        self.logger.addHandler(self.terminal_handler)
        self.logger.addHandler(self.file_handler)

        self.print_format = "{} ({}:{}) - {}"

    @staticmethod
    def get_call_info():
        stack = inspect.stack()

        filename = os.path.normpath(stack[2][1])
        caller = stack[2][3]
        line = stack[2][2]

        return filename, caller, line

    def debug(self, message, *args, **kwargs):
        message = self.print_format.format(*self.get_call_info(), message)
        self.logger.debug(
            message.format(self.caller, self.line, self.filename),
            *args,
            **kwargs,
            stack_info=True
        )

    def info(self, message, *args, **kwargs):
        message = self.print_format.format(*self.get_call_info(), message)
        self.logger.info(message, *args, **kwargs)

    def warning(self, message, *args, **kwargs):
        message = self.print_format.format(*self.get_call_info(), message)
        self.logger.warning(message, *args, **kwargs)

    def error(self, message, *args, **kwargs):
        message = self.print_format.format(*self.get_call_info(), message)
        self.logger.error(message, *args, **kwargs)

    def critical(self, message, *args, **kwargs):
        message = self.print_format.format(*self.get_call_info(), message)
        self.logger.critical(message, *args, **kwargs)


logger = Logger()
