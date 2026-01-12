# Pflichtenheft: Password Generator

## Expected Functionality
This script generates secure random passwords and passphrases with customizable criteria. It uses the `secrets` module for cryptographically strong randomness and includes password strength evaluation.

## Input
- **Function parameters**:
  - `length` (int): Password length (default: 12)
  - `use_uppercase` (bool): Include uppercase letters
  - `use_lowercase` (bool): Include lowercase letters
  - `use_digits` (bool): Include digits
  - `use_special` (bool): Include special characters
  - `word_count` (int): Number of words in passphrase
  - `separator` (str): Separator for passphrase words

## Expected Output
```
Password Generator Demo

1. Standard password (12 characters):
aB3$xK9#mP2Q

2. Long password (20 characters):
vR8@nF4%tL2!pY6#qW9$

3. Alphanumeric only:
mK5nB8qT3wX7

4. Passphrase:
dragon-sunset-ocean-knight

5. Password strength evaluation:
  'abc123': Weak
  'AbC123!@#': Strong
  'VerySecureP@ssw0rd2024': Very Strong
```

## Tests

### Test 1: Generate Standard Password
**Input:** `generate_password(12)`  
**Expected Output:** 12-character string with mixed characters

### Test 2: Generate Long Password
**Input:** `generate_password(20)`  
**Expected Output:** 20-character string

### Test 3: Alphanumeric Only
**Input:** `generate_password(12, use_special=False)`  
**Expected Output:** 12-character string without special characters

### Test 4: Generate Passphrase
**Input:** `generate_passphrase(4)`  
**Expected Output:** String with 4 words separated by hyphens

### Test 5: Password Strength - Weak
**Input:** `password_strength("abc123")`  
**Expected Output:** `"Weak"`

### Test 6: Password Strength - Very Strong
**Input:** `password_strength("VerySecureP@ssw0rd2024")`  
**Expected Output:** `"Very Strong"`

## Dependencies
- Standard library only (random, string, secrets)

## Usage
```bash
python script.py
```
