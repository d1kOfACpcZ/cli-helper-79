import os
import json
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_json_file(filepath):
    """Reads a JSON file and returns its contents as a dictionary."""
    if not os.path.exists(filepath):
        logging.error(f'File not found: {filepath}')
        return None
    with open(filepath, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
            logging.info(f'File read successfully: {filepath}')
            return data
        except json.JSONDecodeError:
            logging.error(f'Error decoding JSON from file: {filepath}')
            return None


def write_json_file(filepath, data):
    """Writes a dictionary to a JSON file."""
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
        logging.info(f'File written successfully: {filepath}')


def list_directory_files(directory):
    """Lists all files in a given directory."""
    try:
        files = os.listdir(directory)
        logging.info(f'Files listed successfully: {directory}')
        return [f for f in files if os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError:
        logging.error(f'Directory not found: {directory}')
        return []


def sanitize_filename(filename):
    """Sanitizes a given filename by removing illegal characters."""
    return ''.join(c for c in filename if c.isalnum() or c in (' ', '.', '_')).rstrip()