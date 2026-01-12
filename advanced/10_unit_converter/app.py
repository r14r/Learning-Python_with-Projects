#!/usr/bin/env python3
"""
Unit Converter Script
Multi-unit conversion system for various measurement types.
"""

from typing import Dict, Optional


# Conversion factors (to base unit)
CONVERSIONS = {
    'length': {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.344,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    },
    'weight': {
        'kilogram': 1.0,
        'gram': 0.001,
        'milligram': 0.000001,
        'pound': 0.453592,
        'ounce': 0.0283495,
        'ton': 1000.0
    },
    'temperature': {
        # Special handling required
    },
    'volume': {
        'liter': 1.0,
        'milliliter': 0.001,
        'gallon': 3.78541,
        'quart': 0.946353,
        'pint': 0.473176,
        'cup': 0.236588,
        'fluid_ounce': 0.0295735
    },
    'time': {
        'second': 1.0,
        'minute': 60.0,
        'hour': 3600.0,
        'day': 86400.0,
        'week': 604800.0,
        'year': 31536000.0
    }
}


def convert_unit(value: float, from_unit: str, to_unit: str, category: str) -> Optional[float]:
    """
    Convert value between units in a category.
    
    Args:
        value (float): Value to convert
        from_unit (str): Source unit
        to_unit (str): Target unit
        category (str): Category (length, weight, volume, time)
    
    Returns:
        float: Converted value, or None if conversion not possible
    """
    if category not in CONVERSIONS:
        return None
    
    units = CONVERSIONS[category]
    
    if from_unit not in units or to_unit not in units:
        return None
    
    # Convert to base unit, then to target unit
    base_value = value * units[from_unit]
    result = base_value / units[to_unit]
    
    return result


def convert_temperature(value: float, from_unit: str, to_unit: str) -> Optional[float]:
    """
    Convert temperature between Celsius, Fahrenheit, and Kelvin.
    
    Args:
        value (float): Temperature value
        from_unit (str): Source unit (celsius, fahrenheit, kelvin)
        to_unit (str): Target unit
    
    Returns:
        float: Converted temperature
    """
    # Convert to Celsius first
    if from_unit == 'celsius':
        celsius = value
    elif from_unit == 'fahrenheit':
        celsius = (value - 32) * 5/9
    elif from_unit == 'kelvin':
        celsius = value - 273.15
    else:
        return None
    
    # Convert from Celsius to target
    if to_unit == 'celsius':
        return celsius
    elif to_unit == 'fahrenheit':
        return celsius * 9/5 + 32
    elif to_unit == 'kelvin':
        return celsius + 273.15
    else:
        return None


def get_available_units(category: str) -> list:
    """
    Get list of available units for a category.
    
    Args:
        category (str): Category name
    
    Returns:
        list: Available units
    """
    if category == 'temperature':
        return ['celsius', 'fahrenheit', 'kelvin']
    return list(CONVERSIONS.get(category, {}).keys())


def get_categories() -> list:
    """
    Get list of available conversion categories.
    
    Returns:
        list: Category names
    """
    return list(CONVERSIONS.keys()) + ['temperature']


def main():
    """Main function to demonstrate unit conversion."""
    print("Unit Converter Demo")
    
    # Length conversions
    print("\n1. Length Conversions:")
    print(f"  5 kilometers = {convert_unit(5, 'kilometer', 'mile', 'length'):.2f} miles")
    print(f"  10 feet = {convert_unit(10, 'foot', 'meter', 'length'):.2f} meters")
    
    # Weight conversions
    print("\n2. Weight Conversions:")
    print(f"  150 pounds = {convert_unit(150, 'pound', 'kilogram', 'weight'):.2f} kilograms")
    print(f"  2 kilograms = {convert_unit(2, 'kilogram', 'gram', 'weight'):.0f} grams")
    
    # Temperature conversions
    print("\n3. Temperature Conversions:")
    print(f"  25°C = {convert_temperature(25, 'celsius', 'fahrenheit'):.2f}°F")
    print(f"  100°F = {convert_temperature(100, 'fahrenheit', 'celsius'):.2f}°C")
    
    # Volume conversions
    print("\n4. Volume Conversions:")
    print(f"  1 gallon = {convert_unit(1, 'gallon', 'liter', 'volume'):.2f} liters")
    print(f"  500 milliliters = {convert_unit(500, 'milliliter', 'cup', 'volume'):.2f} cups")
    
    # Time conversions
    print("\n5. Time Conversions:")
    print(f"  2 hours = {convert_unit(2, 'hour', 'second', 'time'):.0f} seconds")
    print(f"  1 week = {convert_unit(1, 'week', 'day', 'time'):.0f} days")
    
    # Available units
    print("\n6. Available Categories:")
    for category in get_categories():
        units = get_available_units(category)
        print(f"  {category}: {', '.join(units[:5])}" + ('...' if len(units) > 5 else ''))


if __name__ == "__main__":
    main()
