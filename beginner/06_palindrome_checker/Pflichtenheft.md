# Pflichtenheft: Palindrome Checker

## Expected Functionality
This script checks whether a given string is a palindrome (reads the same forwards and backwards). It includes both a case-insensitive version that ignores spaces and a strict version.

## Input
- **Function parameter**: `text` (string)

## Expected Output
```
Palindrome Checker Demo
'racecar' is a palindrome
'hello' is not a palindrome
'A man a plan a canal Panama' is a palindrome
'noon' is a palindrome
'python' is not a palindrome
```

## Tests

### Test 1: Simple Palindrome
**Input:** `is_palindrome("racecar")`  
**Expected Output:** `True`

### Test 2: Not a Palindrome
**Input:** `is_palindrome("hello")`  
**Expected Output:** `False`

### Test 3: Palindrome with Mixed Case
**Input:** `is_palindrome("RaceCar")`  
**Expected Output:** `True`

### Test 4: Palindrome with Spaces
**Input:** `is_palindrome("A man a plan a canal Panama")`  
**Expected Output:** `True`

### Test 5: Single Character
**Input:** `is_palindrome("a")`  
**Expected Output:** `True`

## Usage
```bash
python script.py
```
