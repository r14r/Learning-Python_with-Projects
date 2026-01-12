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


def set_nested_value(data: Dict, path: str, value: Any, separator: str = '.') -> Dict:
    """
    Set value in nested JSON using dot notation.
    
    Args:
        data (dict): JSON data
        path (str): Path to value
        value: Value to set
        separator (str): Path separator
    
    Returns:
        dict: Modified data
    """
    keys = path.split(separator)
    current = data
    
    for key in keys[:-1]:
        if key not in current or not isinstance(current[key], dict):
            current[key] = {}
        current = current[key]
    
    current[keys[-1]] = value
    return data


def flatten_json(data: Dict, parent_key: str = '', separator: str = '.') -> Dict:
    """
    Flatten nested JSON structure.
    
    Args:
        data (dict): Nested JSON data
        parent_key (str): Parent key prefix
        separator (str): Key separator
    
    Returns:
        dict: Flattened JSON
    """
    items = []
    
    for key, value in data.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        
        if isinstance(value, dict):
            items.extend(flatten_json(value, new_key, separator).items())
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict):
                    items.extend(flatten_json(item, f"{new_key}[{i}]", separator).items())
                else:
                    items.append((f"{new_key}[{i}]", item))
        else:
            items.append((new_key, value))
    
    return dict(items)


def merge_json(base: Dict, update: Dict) -> Dict:
    """
    Deep merge two JSON objects.
    
    Args:
        base (dict): Base JSON object
        update (dict): JSON object with updates
    
    Returns:
        dict: Merged JSON
    """
    result = base.copy()
    
    for key, value in update.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_json(result[key], value)
        else:
            result[key] = value
    
    return result


def main():
    """Main function to demonstrate JSON parsing."""
    print("JSON Parser Demo")
    
    # Sample JSON data
    sample_data = {
        "user": {
            "name": "John Doe",
            "email": "john@example.com",
            "address": {
                "city": "New York",
                "country": "USA"
            }
        },
        "orders": [
            {"id": 1, "total": 100},
            {"id": 2, "total": 250}
        ]
    }
    
    # Write to file
    temp_file = "/tmp/sample.json"
    write_json(temp_file, sample_data)
    print(f"\nCreated sample JSON: {temp_file}")
    
    # Read back
    data = read_json(temp_file)
    print(f"\nUser name: {get_nested_value(data, 'user.name')}")
    print(f"User city: {get_nested_value(data, 'user.address.city')}")
    
    # Set nested value
    set_nested_value(data, 'user.phone', '+1234567890')
    print(f"\nAdded phone: {get_nested_value(data, 'user.phone')}")
    
    # Flatten
    flattened = flatten_json(data)
    print("\nFlattened JSON:")
    for key, value in list(flattened.items())[:5]:  # Show first 5
        print(f"  {key}: {value}")
    
    # Merge
    update_data = {
        "user": {
            "age": 30,
            "address": {
                "zip": "10001"
            }
        }
    }
    merged = merge_json(sample_data, update_data)
    print(f"\nAfter merge - User age: {merged['user']['age']}")
    print(f"After merge - City (preserved): {merged['user']['address']['city']}")
    print(f"After merge - Zip (added): {merged['user']['address']['zip']}")


if __name__ == "__main__":
    main()
