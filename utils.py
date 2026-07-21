import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, delay=2):
    """
    Make a network request with retry logic.
    
    :param url: The URL to send the request to.
    :param max_retries: Maximum number of retry attempts.
    :param delay: Delay between attempts in seconds.
    :return: Response object if successful, None if failed.
    """
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response
        except RequestException as e:
            print(f'Error on attempt {attempt + 1}: {e}')  
            attempt += 1
            time.sleep(delay)
    print('Max retries reached. Request failed.')
    return None
