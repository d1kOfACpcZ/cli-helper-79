import time
import random

class Retry:
    def __init__(self, max_attempts=3, delay=1, backoff=2):
        self.max_attempts = max_attempts
        self.delay = delay
        self.backoff = backoff

    def execute(self, function, *args, **kwargs):
        attempts = 0
        while attempts < self.max_attempts:
            try:
                return function(*args, **kwargs)
            except Exception as e:
                attempts += 1
                if attempts == self.max_attempts:
                    raise e
                time.sleep(self.delay)
                self.delay *= self.backoff

# Usage example:
# retry = Retry(max_attempts=5, delay=2)
# result = retry.execute(some_network_function, arg1, arg2)