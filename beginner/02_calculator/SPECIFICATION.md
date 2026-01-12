# Pflichtenheft: Simple Calculator

## Expected Functionality
A calculator that performs four basic arithmetic operations: addition, subtraction, multiplication, and division. The script includes error handling for division by zero.

## Input
- **Function parameters**: Two numbers (int or float)
  - `a`: First operand
  - `b`: Second operand

## Expected Output
For the demonstration:
```
Simple Calculator Demo
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
Error: Cannot divide by zero
```

## Tests

### Test 1: Addition
**Input:** `add(10, 5)`  
**Expected Output:** `15`

### Test 2: Subtraction with Negative Result
**Input:** `subtract(5, 10)`  
**Expected Output:** `-5`

### Test 3: Multiplication
**Input:** `multiply(7, 8)`  
**Expected Output:** `56`

### Test 4: Division
**Input:** `divide(20, 4)`  
**Expected Output:** `5.0`

### Test 5: Division by Zero
**Input:** `divide(10, 0)`  
**Expected Output:** Raises `ValueError` with message "Cannot divide by zero"

## Usage
```bash
python script.py
```
