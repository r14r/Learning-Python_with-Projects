#!/usr/bin/env python3
"""
Basic File Reader Script
Reads and displays content from text files.
"""

import os

def read_file(filename):
    """
    Read and return the content of a file.
    
    Args:
        filename (str): Path to the file
    
    Returns:
        str: File content or error message
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: Permission denied to read '{filename}'"

def read_file_lines(filename):
    """
    Read file and return as list of lines.
    
    Args:
        filename (str): Path to the file
    
    Returns:
        list: List of lines or empty list on error
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.readlines()
    except (FileNotFoundError, PermissionError):
        return []

def main():
    try:
        print(read_file("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
