# Pflichtenheft: Unit Converter

## Expected Functionality
A comprehensive unit conversion system supporting multiple measurement categories: length, weight, temperature, volume, and time. Uses conversion factors and special handling for temperature scales.

## Input
- **Function parameters**:
  - `value` (float): Value to convert
  - `from_unit` (str): Source unit
  - `to_unit` (str): Target unit
  - `category` (str): Measurement category

## Expected Output
```
Unit Converter Demo

1. Length Conversions:
  5 kilometers = 3.11 miles
  10 feet = 3.05 meters

2. Weight Conversions:
  150 pounds = 68.04 kilograms
  2 kilograms = 2000 grams

3. Temperature Conversions:
  25°C = 77.00°F
  100°F = 37.78°C

4. Volume Conversions:
  1 gallon = 3.79 liters
  500 milliliters = 2.11 cups

5. Time Conversions:
  2 hours = 7200 seconds
  1 week = 7 days

6. Available Categories:
  length: meter, kilometer, centimeter, millimeter, mile...
  weight: kilogram, gram, milligram, pound, ounce...
  temperature: celsius, fahrenheit, kelvin
  volume: liter, milliliter, gallon, quart, pint...
  time: second, minute, hour, day, week...
```

## Tests

### Test 1: Length Conversion
**Input:** `convert_unit(1, 'meter', 'centimeter', 'length')`  
**Expected Output:** `100.0`

### Test 2: Weight Conversion
**Input:** `convert_unit(1, 'kilogram', 'pound', 'weight')`  
**Expected Output:** ~`2.20462`

### Test 3: Temperature - Celsius to Fahrenheit
**Input:** `convert_temperature(0, 'celsius', 'fahrenheit')`  
**Expected Output:** `32.0`

### Test 4: Volume Conversion
**Input:** `convert_unit(1, 'liter', 'milliliter', 'volume')`  
**Expected Output:** `1000.0`

### Test 5: Time Conversion
**Input:** `convert_unit(60, 'minute', 'hour', 'time')`  
**Expected Output:** `1.0`

### Test 6: Invalid Conversion
**Input:** `convert_unit(1, 'meter', 'invalid', 'length')`  
**Expected Output:** `None`

## Dependencies
- Standard library only (typing)

## Usage
```bash
python script.py
```
