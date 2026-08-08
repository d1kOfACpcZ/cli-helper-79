import json
from typing import Any, Dict, List


def load_json(file_path: str) -> Dict[str, Any]:
    """Loads a JSON file and returns the data as a dictionary."""
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(file_path: str, data: Dict[str, Any]) -> None:
    """Saves a dictionary as a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_data(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    """Filters a list of dictionaries based on a key-value pair."""
    return [item for item in data if item.get(key) == value] 


def merge_dictionaries(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merges two dictionaries into one, with dict2 values overwriting dict1."""
    merged = dict1.copy()  # Start with the first dictionary
    merged.update(dict2)   # Update with the second dictionary
    return merged


def main():
    # Example usage of utility functions
    data = load_json('data.json')  # Load JSON data
    filtered_data = filter_data(data, 'status', 'active')  # Filter data
    save_json('filtered_data.json', filtered_data)  # Save filtered data

if __name__ == '__main__':
    main()  
