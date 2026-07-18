import time
import requests

class NetworkError(Exception):
    pass

def retry_on_failure(max_retries=3, delay=2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except (requests.ConnectionError, requests.Timeout) as e:
                    retries += 1
                    print(f"Attempt {retries} failed: {e}")
                    time.sleep(delay)
                    if retries == max_retries:
                        raise NetworkError(f"Max retries exceeded for {func.__name__}")
        return wrapper
    return decorator

@retry_on_failure(max_retries=5, delay=3)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
