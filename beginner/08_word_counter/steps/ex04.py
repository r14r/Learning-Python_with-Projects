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

def count_lines(text):
    """Count the number of lines in text."""
    if not text:
        return 0
    return len(text.split('\n'))

def word_frequency(text):
    """
    Count frequency of each word in text.
    
    Returns:
        dict: Dictionary with words as keys and counts as values
    """
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def main():
    try:
        print(count_words("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
