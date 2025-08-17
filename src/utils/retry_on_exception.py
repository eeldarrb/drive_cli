import time
import functools


def retry_on_exception(max_attempts=2, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            caught_exception = None
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    time.sleep(delay)
                    attempt += 1
                    caught_exception = e
            if caught_exception is not None:
                raise caught_exception

        return wrapper

    return decorator
