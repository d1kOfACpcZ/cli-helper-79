import os
import json
from typing import Any, Dict

class FileReadError(Exception):
    pass

class JSONDecodeError(Exception):
    pass


def read_json_file(file_path: str) -> Dict[str, Any]:
    """
    Reads a JSON file and returns its contents as a dictionary.
    Raises:
        FileReadError: If the file cannot be accessed.
        JSONDecodeError: If the JSON is malformed.
    """
    if not os.path.isfile(file_path):
        raise FileReadError(f"File not found: {file_path}")

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        raise JSONDecodeError(f"JSON decode error in file: {file_path}")
    except Exception as e:
        raise FileReadError(f"An error occurred: {str(e)}")

    return data


def save_json_file(data: Dict[str, Any], file_path: str) -> None:
    """
    Saves a dictionary to a JSON file.
    Raises:
        FileReadError: If the file cannot be accessed.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise FileReadError(f"Unable to save file: {str(e)}")
