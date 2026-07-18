import json
import os

DEFAULT_CONFIG = {
    'setting1': 'default_value1',
    'setting2': 'default_value2',
    'setting3': True,
}

class ConfigLoader:
    def __init__(self, config_file=None):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()  # Start with default values
        if self.config_file:
            self.load_config(self.config_file)

    def load_config(self, config_file):
        if os.path.exists(config_file):
            with open(config_file, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)  # Update with user-defined values
        else:
            print(f'Config file {config_file} does not exist. Using defaults.')

    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value

# Example usage:
# loader = ConfigLoader('path/to/config.json')
# print(loader.get('setting1'))
