# Pflichtenheft: List Operations

## Expected Functionality
This script demonstrates basic list operations including finding maximum/minimum values, calculating averages, and removing duplicates while preserving order.

## Input
- **Function parameter**: `numbers` or `items` (list)

## Expected Output
```
List Operations Demo
Original list: [5, 2, 8, 2, 9, 1, 5, 3]
Maximum: 9
Minimum: 1
Average: 4.38
Without duplicates: [5, 2, 8, 9, 1, 3]
```

## Tests

### Test 1: Find Maximum
**Input:** `find_max([5, 2, 8, 2, 9, 1])`  
**Expected Output:** `9`

### Test 2: Find Minimum
**Input:** `find_min([5, 2, 8, 2, 9, 1])`  
**Expected Output:** `1`

### Test 3: Calculate Average
**Input:** `calculate_average([2, 4, 6, 8])`  
**Expected Output:** `5.0`

### Test 4: Remove Duplicates
**Input:** `remove_duplicates([1, 2, 2, 3, 1, 4])`  
**Expected Output:** `[1, 2, 3, 4]`

### Test 5: Empty List
**Input:** `find_max([])`  
**Expected Output:** `None`

## Usage
```bash
python script.py
```
