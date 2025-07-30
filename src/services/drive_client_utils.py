import time
import functools
from googleapiclient.http import HttpError


def retry_on_http_error(max_attempts=2, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            http_err = None
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except HttpError as e:
                    time.sleep(delay)
                    attempt += 1
                    http_err = e
            if http_err is not None:
                raise http_err

        return wrapper

    return decorator
