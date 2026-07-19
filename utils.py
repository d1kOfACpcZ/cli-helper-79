import json


def load_json(file_path):
    """Loads a JSON file and returns its contents as a dictionary."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error loading JSON: {e}')
        return None


def save_json(data, file_path):
    """Saves a dictionary as a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f'Successfully saved data to {file_path}')
    except IOError as e:
        print(f'Error saving JSON: {e}')


def update_dict(original, updates):
    """Updates the original dictionary with values from the updates dictionary."""
    if not isinstance(original, dict) or not isinstance(updates, dict):
        raise ValueError('Both original and updates must be dictionaries.')
    original.update(updates)
    return original


def pretty_print_json(data):
    """Prints a dictionary as a formatted JSON string."""
    print(json.dumps(data, indent=4))
