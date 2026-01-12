#!/usr/bin/env python3
"""
Palindrome Checker Script
Checks if a given string is a palindrome (reads the same forwards and backwards).
"""

def is_palindrome(text):
    """
    Check if a string is a palindrome.
    
    Args:
        text (str): The text to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Remove spaces and convert to lowercase for comparison
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def is_palindrome_strict(text):
    """
    Check if a string is a palindrome (case-sensitive, includes spaces).
    
    Args:
        text (str): The text to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    return text == text[::-1]

def main():
    """Main function to demonstrate palindrome checking."""
    test_words = [
        "racecar",
        "hello",
        "A man a plan a canal Panama",
        "noon",
        "python"
    ]
    
    print("Palindrome Checker Demo")
    for word in test_words:
        result = is_palindrome(word)
        print(f"'{word}' is {'a palindrome' if result else 'not a palindrome'}")

def main():
    try:
        print(is_palindrome("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
