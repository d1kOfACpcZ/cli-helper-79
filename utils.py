import json

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    """Save data as JSON to a file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_dicts(dict1, dict2):
    """Merge two dictionaries into one, with dict2 values overwriting dict1."""
    merged = dict1.copy()  # Create a copy of dict1
    merged.update(dict2)   # Update with dict2 values
    return merged


def read_csv(file_path):
    """Read a CSV file and return a list of dictionaries."""
    import csv
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


def write_csv(data, file_path):
    """Write a list of dictionaries to a CSV file."""
    if not data:
        return  # If data is empty, do not write
    keys = data[0].keys()  # Get the keys from the first dict
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)