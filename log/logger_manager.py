"""Logging class for UmbrellaRL."""

import logging

from log.ilogger import ILogger

class LoggerManager(ILogger):
    _loggers: dict[str, logging.Logger] = {}

    def get_logger(self, module_name: str) -> logging.Logger:
        if module_name not in LoggerManager._loggers:
            logger = logging.getLogger(module_name)
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
            LoggerManager._loggers[module_name] = logger
        return LoggerManager._loggers[module_name]
