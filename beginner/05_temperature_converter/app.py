#!/usr/bin/env python3
"""
Temperature Converter Script
Converts temperatures between Celsius, Fahrenheit, and Kelvin.
"""


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15


def main():
    """Main function to demonstrate temperature conversions."""
    print("Temperature Converter Demo")
    
    celsius = 25
    print(f"\n{celsius}°C equals:")
    print(f"  {celsius_to_fahrenheit(celsius):.2f}°F")
    print(f"  {celsius_to_kelvin(celsius):.2f}K")
    
    fahrenheit = 77
    print(f"\n{fahrenheit}°F equals:")
    print(f"  {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    
    kelvin = 298.15
    print(f"\n{kelvin}K equals:")
    print(f"  {kelvin_to_celsius(kelvin):.2f}°C")


if __name__ == "__main__":
    main()
