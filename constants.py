import os

# Constants for file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, 'config')
LOG_PATH = os.path.join(BASE_DIR, 'logs')

# File extensions
TEXT_EXTENSION = '.txt'
JSON_EXTENSION = '.json'
CSV_EXTENSION = '.csv'

# Settings
DEFAULT_ENCODING = 'utf-8'
MAX_RETRIES = 5
TIMEOUT_SECONDS = 30

# Common messages
ERROR_MESSAGE = 'An error occurred'
SUCCESS_MESSAGE = 'Operation completed successfully'

# Return codes
EXIT_SUCCESS = 0
EXIT_FAILURE = 1

# Log levels
LOG_LEVELS = {
    'debug': 10,
    'info': 20,
    'warning': 30,
    'error': 40,
    'critical': 50
}

# API URLs
API_BASE_URL = 'https://api.example.com'
USER_ENDPOINT = '/users'
POST_ENDPOINT = '/posts'