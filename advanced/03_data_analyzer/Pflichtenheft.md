# Pflichtenheft: Data Analyzer

## Expected Functionality
This script performs data analysis operations using pandas, including calculating statistics, grouping data, and filtering based on conditions.

## Input
- **DataFrame**: Sample data with columns: name, age, salary, department
- **Function parameters**:
  - `column` (str): Column name for analysis
  - `group_by` (str): Column to group by
  - `agg_column` (str): Column to aggregate
  - `operator` (str): Comparison operator ('>', '<', '==', '>=', '<=')
  - `value`: Comparison value

## Expected Output
```
Data Analyzer Demo

Sample Data:
      name  age  salary department
0    Alice   25   50000         IT
1      Bob   30   60000         HR
2  Charlie   35   75000         IT
3    David   28   55000    Finance
4      Eve   32   70000         IT

Salary Statistics:
  mean: 62,000.00
  median: 60,000.00
  std: 10,198.04
  min: 50,000.00
  max: 75,000.00
  count: 5

Department Analysis:
             mean    sum  count
department                     
Finance   55000.0  55000      1
HR        60000.0  60000      1
IT        65000.0 195000      3

Employees with salary > 60000:
      name  salary
2  Charlie   75000
4      Eve   70000
```

## Tests

### Test 1: Basic Statistics
**Input:** `basic_statistics(df, 'salary')`  
**Expected Output:** Dictionary with mean, median, std, min, max, count

### Test 2: Group Analysis
**Input:** `group_analysis(df, 'department', 'salary')`  
**Expected Output:** DataFrame with aggregated statistics per department

### Test 3: Filter Greater Than
**Input:** `filter_data(df, 'age', '>', 30)`  
**Expected Output:** DataFrame with rows where age > 30

### Test 4: Filter Equals
**Input:** `filter_data(df, 'department', '==', 'IT')`  
**Expected Output:** DataFrame with IT department employees

### Test 5: Non-existent Column
**Input:** `basic_statistics(df, 'nonexistent')`  
**Expected Output:** Dictionary with 'error' key

## Dependencies
```
pandas
```

## Usage
```bash
pip install pandas
python script.py
```
