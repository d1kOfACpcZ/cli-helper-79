import json
import os

DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 8080,
    'debug': False,
    'log_level': 'INFO',
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = {}
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                self.config = json.load(file)
        else:
            self.config = DEFAULT_CONFIG

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.get('host'))  # Example usage
