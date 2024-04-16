#!/usr/bin/python3
"""Class to JSON module"""

def class_to_json(obj):
    """Converts an object to a JSON serializable dictionary."""
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    elif hasattr(obj, "__slots__"):
        return {slot: getattr(obj, slot) for slot in getattr(obj, "__slots__")}
    else:
        raise TypeError("Object is not serializable to JSON")
