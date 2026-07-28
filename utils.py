import json
import os


def read_json(file_path):
    """Reads a JSON file and returns its content as a dictionary."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(file_path, data):
    """Writes a dictionary to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def list_files(directory):
    """Lists all files in the given directory."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def merge_dictionaries(dict1, dict2):
    """Merges two dictionaries into one."""
    merged = dict1.copy()  # start with dict1's keys and values
    merged.update(dict2)   # modifies merged with dict2's keys and values
    return merged


def generate_random_string(length=10):
    """Generates a random string of fixed length."""
    import random
    import string
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))
