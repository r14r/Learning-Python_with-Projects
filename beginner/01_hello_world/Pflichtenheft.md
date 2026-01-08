# Pflichtenheft: Hello World

## Expected Functionality
This script demonstrates the most basic Python program - printing a greeting message. It includes a function that can greet with a default or custom name.

## Input
- **Function parameter**: `name` (string, optional, default: "World")
- No command-line arguments required for basic execution

## Expected Output
```
Hello, World!
Hello, Python Learner!
```

## Tests

### Test 1: Default Greeting
**Input:** `greet()`  
**Expected Output:** `"Hello, World!"`

### Test 2: Custom Name
**Input:** `greet("Alice")`  
**Expected Output:** `"Hello, Alice!"`

### Test 3: Empty String
**Input:** `greet("")`  
**Expected Output:** `"Hello, !"`

### Test 4: Special Characters
**Input:** `greet("José")`  
**Expected Output:** `"Hello, José!"`

## Usage
```bash
python script.py
```
