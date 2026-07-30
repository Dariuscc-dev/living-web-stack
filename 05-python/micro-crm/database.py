import json
import os

FILE_NAME = "data.json"

def load_data():
    """Reads the JSON file and returns a list of dictionaries."""
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        # Handles the error if the JSON is empty or corrupted
        return []

def save_data(data_list):
    """Writes the list of dictionaries back to the JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data_list, file, indent=4)
