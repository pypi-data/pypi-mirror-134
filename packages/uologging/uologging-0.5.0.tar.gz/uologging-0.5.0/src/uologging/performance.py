import time
import logging
from functools import wraps


def trace(logger: logging.Logger):
    """Decorator to trace the execution time of a Python function or method.

    Args:
        logger (logging.Logger): The logger instance for the function's module.

    Example:

    First, get the logger for your Python module.

        import logging
        logger = logging.getLogger(__name__)

    Then, use the trace_time decorator with that logger as the argument.

        import uologging
        @uologging.trace(logger)
        def my_slow_function():
            import time
            time.sleep(1)
        my_slow_function()
    """
    def _trace_time(func):
        @wraps(func)
        def timed(*args, **kw_args):
            func_str_repr = f'{func.__module__}:{func.__name__}({args!r},{kw_args!r})'
            logger.debug(f'Starting: {func_str_repr}')
            start = time.time()
            result = func(*args, **kw_args)
            end = time.time()
            logger.debug(f'Finished: {func_str_repr}')
            logger.info(f'{func_str_repr} exec time: {end - start:.2f} sec')
            return result
        return timed
    return _trace_time
