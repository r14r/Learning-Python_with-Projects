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

def to_title_case(text):
    """Convert string to title case."""
    return text.title()

def remove_whitespace(text):
    """Remove all whitespace from a string."""
    return "".join(text.split())

def main():
    """Main function to demonstrate string operations."""
    sample_text = "hello world"
    
    print("String Operations Demo")
    print(f"Original: '{sample_text}'")
    print(f"Reversed: '{reverse_string(sample_text)}'")
    print(f"Vowel count: {count_vowels(sample_text)}")
    print(f"Title case: '{to_title_case(sample_text)}'")
    print(f"No whitespace: '{remove_whitespace(sample_text)}'")

def main():
    try:
        print(reverse_string("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
