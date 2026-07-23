import json
import os

DEFAULTS = {
    'host': 'localhost',
    'port': 8080,
    'debug': False
}

def load_config(file_path):
    """Load configuration from a JSON file or use defaults if not found."""
    config = DEFAULTS.copy()
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            user_config = json.load(f)
            config.update(user_config)
    return config
