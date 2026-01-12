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

def main():
    try:
        print(validate_email("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
