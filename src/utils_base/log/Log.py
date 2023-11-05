"""Utils."""

import logging

from utils_base.log.Console import Console
from utils_base.log.constants import LEVEL_TO_STYLE


class CustomLoggingFormatter(logging.Formatter):
    def format(self, record):
        style = LEVEL_TO_STYLE[record.levelno]
        return Console.format(
            (f'[{record.name}] ' if record.name else ''),
            record.msg,
            **style,
        )


class Log(logging.Logger):
    def __init__(self, name: str, level: int = logging.DEBUG):
        super(Log, self).__init__(name, level)
        self.propagate = False

        formatter = CustomLoggingFormatter()
        sh = logging.StreamHandler()
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(formatter)
        self.handlers = [sh]  # noqa


_log = Log('')