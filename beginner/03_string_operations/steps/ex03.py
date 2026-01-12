#!/usr/bin/env python3
"""
String Operations Script
Demonstrates various string manipulation operations.
"""

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def count_vowels(text):
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def main():
    try:
        print(reverse_string("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
