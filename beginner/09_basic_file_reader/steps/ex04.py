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

def count_file_lines(filename):
    """Count the number of lines in a file."""
    lines = read_file_lines(filename)
    return len(lines)

def main():
    """Main function to demonstrate file reading."""
    # Create a sample file for demonstration
    sample_file = "sample.txt"
    with open(sample_file, 'w', encoding='utf-8') as f:
        f.write("Line 1: Hello World\n")
        f.write("Line 2: Python File Reader\n")
        f.write("Line 3: End of file\n")
    
    print("Basic File Reader Demo")
    print(f"\nReading file: {sample_file}")
    content = read_file(sample_file)
    print(content)
    
    print(f"\nNumber of lines: {count_file_lines(sample_file)}")
    
    # Clean up
    os.remove(sample_file)

def main():
    try:
        print(read_file("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
