import json
import os
from collections import defaultdict

def load_config(file_path, defaults):
    """Load configuration from a JSON file with defaults."""
    # Create a defaultdict to hold the merged configurations
    config = defaultdict(lambda: None, defaults)

    # If the config file exists, read the content
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                # Update the config with values from the file
                file_config = json.load(file)
                config.update(file_config)
            except json.JSONDecodeError as e:
                print(f'Error loading config: {e}')
    else:
        print(f'Config file {file_path} not found. Using defaults.')  

    return dict(config)

# Example of default configuration
if __name__ == '__main__':
    default_config = {
        'host': 'localhost',
        'port': 8080,
        'debug': False
    }
    config = load_config('config.json', default_config)
    print(config)