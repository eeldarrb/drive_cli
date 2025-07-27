import time
import functools
from googleapiclient.http import HttpError


def retry_on_http_error(max_attempts=2, delay=1):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			attempt = 0
			err_status = None
			while attempt < max_attempts:
				try:
					return func(*args, **kwargs)
				except HttpError as e:
					err_status = e.status_code
					time.sleep(delay)
					attempt += 1
			raise RuntimeError(f"HTTP Error. Server responded with {err_status}.")

		return wrapper

	return decorator
