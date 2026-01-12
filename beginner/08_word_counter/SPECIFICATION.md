# Pflichtenheft: Word Counter

## Expected Functionality
This script analyzes text and provides statistics including word count, character count (with/without spaces), line count, and word frequency analysis.

## Input
- **Function parameter**: `text` (string)

## Expected Output
```
Word Counter Demo
Text:
Hello world
This is a sample text
Hello Python world

Words: 9
Characters (with spaces): 47
Characters (without spaces): 39
Lines: 3

Word frequency: {'hello': 2, 'world': 2, 'this': 1, 'is': 1, 'a': 1, 'sample': 1, 'text': 1, 'python': 1}
```

## Tests

### Test 1: Count Words
**Input:** `count_words("Hello world from Python")`  
**Expected Output:** `4`

### Test 2: Count Words - Empty String
**Input:** `count_words("")`  
**Expected Output:** `0`

### Test 3: Count Characters With Spaces
**Input:** `count_characters("Hello", include_spaces=True)`  
**Expected Output:** `5`

### Test 4: Count Lines
**Input:** `count_lines("Line 1\nLine 2\nLine 3")`  
**Expected Output:** `3`

### Test 5: Word Frequency
**Input:** `word_frequency("hello world hello")`  
**Expected Output:** `{'hello': 2, 'world': 1}`

## Usage
```bash
python script.py
```
