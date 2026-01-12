#!/usr/bin/env python3
"""
Regular Expression Tool Script
Utility functions for working with regular expressions.
"""

import re
from typing import List, Dict, Optional, Pattern

def validate_email(email: str) -> bool:
    """
    Validate email address format.
    
    Args:
        email (str): Email address to validate
    
    Returns:
        bool: True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str, format_type: str = 'us') -> bool:
    """
    Validate phone number format.
    
    Args:
        phone (str): Phone number to validate
        format_type (str): Format type ('us', 'international')
    
    Returns:
        bool: True if valid, False otherwise
    """
    patterns = {
        'us': r'^\+?1?[-.\s]?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$',
        'international': r'^\+[1-9]\d{1,14}$'
    }
    pattern = patterns.get(format_type, patterns['us'])
    return bool(re.match(pattern, phone))

def extract_urls(text: str) -> List[str]:
    """
    Extract all URLs from text.
    
    Args:
        text (str): Text to search
    
    Returns:
        List[str]: List of URLs found
    """
    pattern = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'
    return re.findall(pattern, text)

def extract_dates(text: str, format_type: str = 'mdy') -> List[str]:
    """
    Extract dates from text.
    
    Args:
        text (str): Text to search
        format_type (str): Date format ('mdy', 'dmy', 'ymd')
    
    Returns:
        List[str]: List of dates found
    """
    patterns = {
        'mdy': r'\b(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/(\d{4}|\d{2})\b',
        'dmy': r'\b(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/(\d{4}|\d{2})\b',
        'ymd': r'\b(\d{4})-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01])\b'
    }
    pattern = patterns.get(format_type, patterns['mdy'])
    matches = re.findall(pattern, text)
    return ['/'.join(m) if format_type != 'ymd' else '-'.join(m) for m in matches]

def replace_pattern(text: str, pattern: str, replacement: str) -> str:
    """
    Replace all occurrences of pattern with replacement.
    
    Args:
        text (str): Input text
        pattern (str): Regular expression pattern
        replacement (str): Replacement string
    
    Returns:
        str: Text with replacements
    """
    return re.sub(pattern, replacement, text)

def split_by_pattern(text: str, pattern: str) -> List[str]:
    """
    Split text by pattern.
    
    Args:
        text (str): Input text
        pattern (str): Regular expression pattern
    
    Returns:
        List[str]: Split parts
    """
    return re.split(pattern, text)

def find_with_context(text: str, pattern: str, context: int = 20) -> List[Dict]:
    """
    Find pattern matches with surrounding context.
    
    Args:
        text (str): Text to search
        pattern (str): Regular expression pattern
        context (int): Characters of context to include
    
    Returns:
        List[Dict]: Matches with context
    """
    results = []
    for match in re.finditer(pattern, text):
        start = max(0, match.start() - context)
        end = min(len(text), match.end() + context)
        results.append({
            'match': match.group(),
            'start': match.start(),
            'end': match.end(),
            'context': text[start:end]
        })
    return results

def main():
    """Main function to demonstrate regex tools."""
    print("Regular Expression Tool Demo")
    
    # Email validation
    print("\n1. Email Validation:")
    emails = ["test@example.com", "invalid.email", "user@domain.co.uk"]
    for email in emails:
        valid = validate_email(email)
        print(f"  {email}: {'Valid' if valid else 'Invalid'}")
    
    # Phone validation
    print("\n2. Phone Validation:")
    phones = ["(555) 123-4567", "+1-555-123-4567", "123-456"]
    for phone in phones:
        valid = validate_phone(phone)
        print(f"  {phone}: {'Valid' if valid else 'Invalid'}")
    
    # Extract URLs
    print("\n3. Extract URLs:")
    text_with_urls = "Visit https://example.com or http://www.test.org for info"
    urls = extract_urls(text_with_urls)
    for url in urls:
        print(f"  Found: {url}")
    
    # Extract dates
    print("\n4. Extract Dates:")
    text_with_dates = "Events on 12/25/2024 and 01/01/2025"
    dates = extract_dates(text_with_dates)
    for date in dates:
        print(f"  Found: {date}")
    
    # Replace pattern
    print("\n5. Replace Pattern:")
    text = "Phone: 555-1234, Code: 555-5678"
    result = replace_pattern(text, r'\d{3}-\d{4}', 'XXX-XXXX')
    print(f"  Original: {text}")
    print(f"  Masked: {result}")

def main():
    try:
        print(validate_email("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
