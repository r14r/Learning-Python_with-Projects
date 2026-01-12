# Pflichtenheft: Regular Expression Tool

## Expected Functionality
A collection of utility functions for common regular expression tasks including validation (email, phone), extraction (URLs, dates), pattern replacement, and text splitting.

## Input
- **Function parameters**:
  - `email` (str): Email address to validate
  - `phone` (str): Phone number to validate
  - `text` (str): Text to process
  - `pattern` (str): Regular expression pattern
  - `replacement` (str): Replacement text
  - `format_type` (str): Format specifier
  - `context` (int): Context characters around matches

## Expected Output
```
Regular Expression Tool Demo

1. Email Validation:
  test@example.com: Valid
  invalid.email: Invalid
  user@domain.co.uk: Valid

2. Phone Validation:
  (555) 123-4567: Valid
  +1-555-123-4567: Valid
  123-456: Invalid

3. Extract URLs:
  Found: https://example.com
  Found: http://www.test.org

4. Extract Dates:
  Found: 12/25/2024
  Found: 01/01/2025

5. Replace Pattern:
  Original: Phone: 555-1234, Code: 555-5678
  Masked: Phone: XXX-XXXX, Code: XXX-XXXX
```

## Tests

### Test 1: Email Validation - Valid
**Input:** `validate_email("test@example.com")`  
**Expected Output:** `True`

### Test 2: Email Validation - Invalid
**Input:** `validate_email("invalid.email")`  
**Expected Output:** `False`

### Test 3: Extract URLs
**Input:** `extract_urls("Visit https://example.com")`  
**Expected Output:** `['https://example.com']`

### Test 4: Extract Dates
**Input:** `extract_dates("Date: 12/25/2024")`  
**Expected Output:** `['12/25/2024']`

### Test 5: Replace Pattern
**Input:** `replace_pattern("abc123", r'\d+', 'XXX')`  
**Expected Output:** `'abcXXX'`

### Test 6: Split by Pattern
**Input:** `split_by_pattern("a,b;c", r'[,;]')`  
**Expected Output:** `['a', 'b', 'c']`

## Dependencies
- Standard library only (re, typing)

## Usage
```bash
python script.py
```
