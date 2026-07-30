import json
import os

DEFAULT_CONFIG = {
    'host': 'localhost',
    'port': 8000,
    'debug': False,
    'log_level': 'INFO'
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()
        self.load_config()

    def load_config(self):
        if os.path.isfile(self.config_file):
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
            self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def __str__(self):
        return json.dumps(self.config, indent=2)

if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader)