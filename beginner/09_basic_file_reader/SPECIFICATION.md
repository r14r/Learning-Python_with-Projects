# Pflichtenheft: Basic File Reader

## Expected Functionality
This script reads text files and displays their content. It includes error handling for common file operations issues like missing files or permission errors.

## Input
- **Function parameter**: `filename` (string) - Path to the text file

## Expected Output
```
Basic File Reader Demo

Reading file: sample.txt
Line 1: Hello World
Line 2: Python File Reader
Line 3: End of file

Number of lines: 3
```

## Tests

### Test 1: Read Existing File
**Input:** `read_file("test.txt")` with existing file  
**Expected Output:** Content of the file as string

### Test 2: Read Non-existent File
**Input:** `read_file("nonexistent.txt")`  
**Expected Output:** `"Error: File 'nonexistent.txt' not found"`

### Test 3: Read File Lines
**Input:** `read_file_lines("test.txt")` with 3-line file  
**Expected Output:** List with 3 elements (one per line)

### Test 4: Count Lines
**Input:** `count_file_lines("test.txt")` with 5-line file  
**Expected Output:** `5`

### Test 5: Empty File
**Input:** `count_file_lines("empty.txt")` with empty file  
**Expected Output:** `0`

## Usage
```bash
python script.py
```

## Notes
The script creates a temporary sample file for demonstration purposes and removes it after execution.
