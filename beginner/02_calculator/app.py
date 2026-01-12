#!/usr/bin/env python3
"""
Simple Calculator Script
Performs basic arithmetic operations: addition, subtraction, multiplication, division.
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """
    Divide a by b.
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    """Main function to demonstrate calculator operations."""
    print("Simple Calculator Demo")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 * 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")
    
    # Example with error handling
    try:
        print(f"10 / 0 = {divide(10, 0)}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
