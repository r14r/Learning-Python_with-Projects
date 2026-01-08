# Pflichtenheft: String Operations

## Expected Functionality
This script demonstrates common string manipulation operations including reversing strings, counting vowels, converting to title case, and removing whitespace.

## Input
- **Function parameter**: `text` (string)

## Expected Output
```
String Operations Demo
Original: 'hello world'
Reversed: 'dlrow olleh'
Vowel count: 3
Title case: 'Hello World'
No whitespace: 'helloworld'
```

## Tests

### Test 1: Reverse String
**Input:** `reverse_string("hello")`  
**Expected Output:** `"olleh"`

### Test 2: Count Vowels
**Input:** `count_vowels("Hello World")`  
**Expected Output:** `3` (e, o, o)

### Test 3: Count Vowels - No Vowels
**Input:** `count_vowels("xyz")`  
**Expected Output:** `0`

### Test 4: Title Case
**Input:** `to_title_case("hello world from python")`  
**Expected Output:** `"Hello World From Python"`

### Test 5: Remove Whitespace
**Input:** `remove_whitespace("  hello   world  ")`  
**Expected Output:** `"helloworld"`

## Usage
```bash
python script.py
```
