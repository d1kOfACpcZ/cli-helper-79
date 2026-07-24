import json
import os


def read_json_file(filepath):
    """Reads a JSON file and returns a dictionary."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'No such file: {filepath}')
    with open(filepath, 'r') as f:
        return json.load(f)


def write_json_file(filepath, data):
    """Writes a dictionary to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)


def list_files(directory):
    """Returns a list of files in a directory."""
    if not os.path.exists(directory):
        raise NotADirectoryError(f'No such directory: {directory}')
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def format_size(size):
    """Converts bytes to a human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f'{size:.2f} {unit}'
        size /= 1024
    return f'{size:.2f} PB'