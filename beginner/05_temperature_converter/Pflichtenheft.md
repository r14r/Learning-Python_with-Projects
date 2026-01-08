# Pflichtenheft: Temperature Converter

## Expected Functionality
This script converts temperatures between Celsius, Fahrenheit, and Kelvin scales using standard conversion formulas.

## Input
- **Function parameter**: Temperature value (int or float)

## Expected Output
```
Temperature Converter Demo

25°C equals:
  77.00°F
  298.15K

77°F equals:
  25.00°C

298.15K equals:
  25.00°C
```

## Tests

### Test 1: Celsius to Fahrenheit - Freezing Point
**Input:** `celsius_to_fahrenheit(0)`  
**Expected Output:** `32.0`

### Test 2: Fahrenheit to Celsius - Boiling Point
**Input:** `fahrenheit_to_celsius(212)`  
**Expected Output:** `100.0`

### Test 3: Celsius to Kelvin - Absolute Zero
**Input:** `celsius_to_kelvin(-273.15)`  
**Expected Output:** `0.0`

### Test 4: Kelvin to Celsius - Room Temperature
**Input:** `kelvin_to_celsius(293.15)`  
**Expected Output:** `20.0`

### Test 5: Round Trip Conversion
**Input:** `fahrenheit_to_celsius(celsius_to_fahrenheit(25))`  
**Expected Output:** `25.0`

## Usage
```bash
python script.py
```
