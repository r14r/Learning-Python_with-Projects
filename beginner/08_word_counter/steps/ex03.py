#!/usr/bin/env python3
"""
Word Counter Script
Counts words, characters, and lines in text.
"""

def count_words(text):
    """Count the number of words in text."""
    if not text.strip():
        return 0
    return len(text.split())

def count_characters(text, include_spaces=True):
    """
    Count the number of characters in text.
    
    Args:
        text (str): The text to analyze
        include_spaces (bool): Whether to include spaces in count
    
    Returns:
        int: Character count
    """
    if include_spaces:
        return len(text)
    else:
        return len(text.replace(" ", ""))

def main():
    try:
        print(count_words("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
