# Pflichtenheft: JSON Parser

## Expected Functionality
This script provides comprehensive JSON manipulation capabilities including reading/writing files, accessing nested values with dot notation, flattening structures, and deep merging objects.

## Input
- **Function parameters**:
  - `filename` (str): Path to JSON file
  - `data` (dict): JSON data
  - `path` (str): Dot-notation path (e.g., 'user.address.city')
  - `value` (Any): Value to set
  - `separator` (str): Path separator (default: '.')
  - `base` (dict): Base JSON for merging
  - `update` (dict): Update JSON for merging

## Expected Output
```
JSON Parser Demo

Created sample JSON: /tmp/sample.json

User name: John Doe
User city: New York

Added phone: +1234567890

Flattened JSON:
  user.name: John Doe
  user.email: john@example.com
  user.address.city: New York
  user.address.country: USA
  orders[0].id: 1

After merge - User age: 30
After merge - City (preserved): New York
After merge - Zip (added): 10001
```

## Tests

### Test 1: Read JSON
**Input:** `read_json("test.json")`  
**Expected Output:** Parsed JSON as dict or list

### Test 2: Get Nested Value
**Input:** `get_nested_value({'a': {'b': 'c'}}, 'a.b')`  
**Expected Output:** `'c'`

### Test 3: Set Nested Value
**Input:** `set_nested_value({}, 'a.b.c', 'value')`  
**Expected Output:** `{'a': {'b': {'c': 'value'}}}`

### Test 4: Flatten JSON
**Input:** `flatten_json({'a': {'b': 1, 'c': 2}})`  
**Expected Output:** `{'a.b': 1, 'a.c': 2}`

### Test 5: Merge JSON
**Input:** `merge_json({'a': 1, 'b': {'c': 2}}, {'b': {'d': 3}})`  
**Expected Output:** `{'a': 1, 'b': {'c': 2, 'd': 3}}`

## Dependencies
- Standard library only (json, typing)

## Usage
```bash
python script.py
```
