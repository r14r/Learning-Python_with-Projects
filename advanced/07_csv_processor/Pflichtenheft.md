# Pflichtenheft: CSV Processor

## Expected Functionality
This script processes CSV files with operations including reading, writing, filtering, aggregating, and transforming data. It handles CSV files with or without headers and provides flexible data manipulation capabilities.

## Input
- **Function parameters**:
  - `filename` (str): Path to CSV file
  - `data` (List[Dict]): CSV data as list of dictionaries
  - `column` (str): Column name for operations
  - `value` (str): Value for filtering
  - `group_by` (str): Column to group by for aggregation
  - `agg_column` (str): Column to aggregate
  - `func`: Transformation function

## Expected Output
```
CSV Processor Demo

Created sample CSV: /tmp/sample.csv

Read 4 rows

IT department employees: 2
  - Alice
  - Charlie

Total salary by department:
  IT: $125,000
  HR: $60,000
  Finance: $55,000

Transformed names:
  ALICE
  BOB
  CHARLIE
  DAVID
```

## Tests

### Test 1: Read CSV
**Input:** `read_csv("test.csv")`  
**Expected Output:** List of dictionaries with CSV data

### Test 2: Write CSV
**Input:** `write_csv("output.csv", [{'a': 1, 'b': 2}])`  
**Expected Output:** File created with header and data

### Test 3: Filter CSV
**Input:** `filter_csv(data, 'department', 'IT')`  
**Expected Output:** List with only IT department rows

### Test 4: Aggregate CSV
**Input:** `aggregate_csv(data, 'department', 'salary')`  
**Expected Output:** Dictionary with sum of salaries per department

### Test 5: Transform Column
**Input:** `transform_column(data, 'name', str.upper)`  
**Expected Output:** Data with names in uppercase

## Dependencies
- Standard library only (csv, typing, io)

## Usage
```bash
python script.py
```
