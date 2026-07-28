import time
import requests


def retry_network_operation(func, retries=3, delay=2, *args, **kwargs):
    """
    Retries a network operation if it fails.
    :param func: The function to call.
    :param retries: Number of retries before giving up.
    :param delay: Delay between retries in seconds.
    :param args: Positional arguments for the function.
    :param kwargs: Keyword arguments for the function.
    :return: The result of the function call.
    """
    for attempt in range(retries):
        try:
            return func(*args, **kwargs)
        except requests.ConnectionError as e:
            if attempt < retries - 1:
                time.sleep(delay)
                print(f'Retry {attempt + 1}/{retries} in {delay} seconds...')
            else:
                print('Max retries exceeded.
                raise e

    return None


# Example usage
if __name__ == '__main__':
    def fetch_data(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    url = 'https://api.example.com/data'
    print(retry_network_operation(fetch_data, url=url))
