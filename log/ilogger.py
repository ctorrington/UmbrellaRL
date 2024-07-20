"""Logging abstract class for UmbrellaRL."""

import logging

from abc import ABC, abstractmethod

class ILogger(ABC):

    @abstractmethod
    def get_logger(self, module_name: str) -> logging.Logger:
        pass
