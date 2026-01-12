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

def main():
    try:
        print(celsius_to_fahrenheit("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
