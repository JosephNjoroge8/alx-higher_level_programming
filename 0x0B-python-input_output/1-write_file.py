#!/usr/bin/python3
def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return the number of characters written"""
    with open(filename, mode="w", encoding="utf-8") as f:
        chars_written = f.write(text)
    return chars_written
