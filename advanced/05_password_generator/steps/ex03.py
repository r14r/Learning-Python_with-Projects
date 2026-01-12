#!/usr/bin/env python3
"""
Password Generator Script
Generates secure random passwords with customizable criteria.
"""

import random
import string
import secrets
from typing import List

def generate_password(
    length: int = 12,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_special: bool = True
) -> str:
    """
    Generate a secure random password.
    
    Args:
        length (int): Password length
        use_uppercase (bool): Include uppercase letters
        use_lowercase (bool): Include lowercase letters
        use_digits (bool): Include digits
        use_special (bool): Include special characters
    
    Returns:
        str: Generated password
    """
    if length < 4:
        raise ValueError("Password length must be at least 4")
    
    character_pool = ""
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("At least one character type must be enabled")
    
    # Use secrets for cryptographically strong random numbers
    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password

def generate_passphrase(word_count: int = 4, separator: str = "-") -> str:
    """
    Generate a passphrase using random words.
    
    Args:
        word_count (int): Number of words in passphrase
        separator (str): Separator between words
    
    Returns:
        str: Generated passphrase
    """
    # Simple word list for demonstration
    words = [
        "apple", "banana", "cherry", "dragon", "eagle", "forest",
        "garden", "horizon", "island", "jungle", "knight", "lemon",
        "mountain", "novel", "ocean", "planet", "queen", "river",
        "sunset", "thunder", "universe", "valley", "winter", "yellow"
    ]
    
    selected_words = [secrets.choice(words) for _ in range(word_count)]
    return separator.join(selected_words)

def main():
    try:
        print(generate_password())
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
