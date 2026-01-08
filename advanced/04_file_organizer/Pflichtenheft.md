# Pflichtenheft: File Organizer

## Expected Functionality
This script organizes files in a directory by extension or modification date. It can create folders for each category and move files accordingly, or simply report the organization structure.

## Input
- **Function parameters**:
  - `source_dir` (str): Directory containing files to organize
  - `create_folders` (bool): Whether to create folders and move files
  - `date_format` (str): Date format for folder names

## Expected Output
```
File Organizer Demo

Created test files in /tmp/file_organizer_test

Files by extension:
  .txt: ['document.txt']
  .jpg: ['image.jpg', 'photo.jpg']
  .py: ['script.py']
  .csv: ['data.csv']

File info for document.txt:
  name: document.txt
  size: 0
  created: 2024-01-08T12:34:56
  modified: 2024-01-08T12:34:56
  extension: .txt
  is_file: True
  is_dir: False
```

## Tests

### Test 1: Organize by Extension
**Input:** `organize_by_extension("/test/dir", create_folders=False)`  
**Expected Output:** Dictionary mapping extensions to file lists

### Test 2: Organize by Date
**Input:** `organize_by_date("/test/dir")`  
**Expected Output:** Dictionary mapping dates to file lists

### Test 3: Get File Info
**Input:** `get_file_info("test.txt")`  
**Expected Output:** Dictionary with file metadata

### Test 4: Non-existent Directory
**Input:** `organize_by_extension("/nonexistent")`  
**Expected Output:** Dictionary with 'error' key

### Test 5: Move Files to Folders
**Input:** `organize_by_extension("/test/dir", create_folders=True)`  
**Expected Output:** Files moved to extension-based folders

## Dependencies
- Standard library only (os, shutil, pathlib, datetime)

## Usage
```bash
python script.py
```
