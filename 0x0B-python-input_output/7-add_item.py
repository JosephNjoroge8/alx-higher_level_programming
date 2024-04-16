#!/usr/bin/python3
"""Adds command line arguments to a list and saves them to a JSON file."""

import sys
import json
from os import path

def save_to_json_file(my_obj, filename):
    """Saves object to a JSON file."""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """Loads object from a JSON file."""
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)

def main():
    """Main function."""
    args = sys.argv[1:]  # Exclude script name from arguments
    filename = 'add_item.json'

    if path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    items.extend(args)  # Add command line arguments to the list

    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
