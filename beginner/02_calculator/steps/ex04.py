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
    print("Step 4: Kernbausteine geladen.")

if __name__ == "__main__":
    main()
