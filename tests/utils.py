"""Utilities for unit testing."""

import time

from logging import Logger
from typing import Callable, Any

from log.logger_manager import LoggerManager

logger: Logger = LoggerManager().get_logger('UnitTestLogger')

def timed(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator method to measure unit test execution time."""
    

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        
        # Measure execution time.
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time

        # Attempt class name.
        class_name = args[0].__class__.__name__ if args else 'oh no'
        logger.debug(f"{class_name}.{func.__name__} ran in {run_time:.6f}s.")

        return result

    return wrapper
