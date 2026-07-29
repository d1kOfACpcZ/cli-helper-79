import json
import os

class ConfigLoader:
    def __init__(self, default_config_path, env_config_path=None):
        self.default_config_path = default_config_path
        self.env_config_path = env_config_path or os.path.join(os.getcwd(), 'config.json')
        self.config = self.load_config()

    def load_config(self):
        # Load default configuration
        config = self.load_json(self.default_config_path)

        # Load environment-specific configuration if it exists
        env_config = self.load_json(self.env_config_path)
        if env_config:
            config.update(env_config)

        return config

    @staticmethod
    def load_json(file_path):
        # Load JSON file and return the data
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                return json.load(f)
        return {}

    def get(self, key, default=None):
        # Retrieve a configuration value by key
        return self.config.get(key, default)

# Example usage
if __name__ == '__main__':
    loader = ConfigLoader('default_config.json')
    api_key = loader.get('API_KEY', 'default_api_key')
    print('API_KEY:', api_key)