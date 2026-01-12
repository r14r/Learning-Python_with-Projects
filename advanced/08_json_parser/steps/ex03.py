#!/usr/bin/env python3
"""
JSON Parser Script
Parse, manipulate, and transform JSON data.
"""

import json
from typing import Any, Dict, List, Optional

def read_json(filename: str) -> Optional[Dict]:
    """
    Read and parse JSON file.
    
    Args:
        filename (str): Path to JSON file
    
    Returns:
        dict or list: Parsed JSON data, or None on error
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON: {e}")
        return None

def write_json(filename: str, data: Any, pretty: bool = True):
    """
    Write data to JSON file.
    
    Args:
        filename (str): Output file path
        data: Data to write
        pretty (bool): Whether to format with indentation
    """
    with open(filename, 'w', encoding='utf-8') as f:
        if pretty:
            json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            json.dump(data, f, ensure_ascii=False)

def get_nested_value(data: Dict, path: str, separator: str = '.') -> Any:
    """
    Get value from nested JSON using dot notation.
    
    Args:
        data (dict): JSON data
        path (str): Path to value (e.g., 'user.address.city')
        separator (str): Path separator
    
    Returns:
        Any: Value at path, or None if not found
    """
    keys = path.split(separator)
    result = data
    
    for key in keys:
        if isinstance(result, dict) and key in result:
            result = result[key]
        else:
            return None
    
    return result

def main():
    try:
        print(read_json("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
