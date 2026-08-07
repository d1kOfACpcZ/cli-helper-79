import json

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'Error: The file {file_path} was not found.')
        return None
    except json.JSONDecodeError:
        print(f'Error: The file {file_path} does not contain valid JSON.')
        return None
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
        return None


def save_json(data, file_path):
    """Save data to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f'Failed to write data to {file_path}: {e}')


def merge_dicts(dict1, dict2):
    """Merge two dictionaries, with dict2 overwriting dict1 keys."""
    return {**dict1, **dict2}


def pretty_print_json(data):
    """Print JSON data in a formatted way."""
    print(json.dumps(data, indent=4))
