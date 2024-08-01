"""Utilities for unit testing."""

import time

from logging import Logger
from typing import Callable, Any

from log.logger_manager import LoggerManager

logger: Logger = LoggerManager().get_logger('UnitTestLogger')

def timed(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator method to measure unit test execution time."""

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        logger.debug(f"{func.__name__} ran in {run_time:.6f}s.")

        return result

    return wrapper
