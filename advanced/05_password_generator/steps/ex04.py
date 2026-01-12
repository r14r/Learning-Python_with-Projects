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

def password_strength(password: str) -> str:
    """
    Evaluate password strength.
    
    Args:
        password (str): Password to evaluate
    
    Returns:
        str: Strength level (Weak, Medium, Strong, Very Strong)
    """
    score = 0
    
    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    
    # Character variety checks
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    
    if score < 3:
        return "Weak"
    elif score < 5:
        return "Medium"
    elif score < 6:
        return "Strong"
    else:
        return "Very Strong"

def main():
    """Main function to demonstrate password generation."""
    print("Password Generator Demo")
    
    print("\n1. Standard password (12 characters):")
    print(generate_password(12))
    
    print("\n2. Long password (20 characters):")
    print(generate_password(20))
    
    print("\n3. Alphanumeric only:")
    print(generate_password(12, use_special=False))
    
    print("\n4. Passphrase:")
    passphrase = generate_passphrase(4)
    print(passphrase)
    
    print("\n5. Password strength evaluation:")
    test_passwords = ["abc123", "AbC123!@#", "VerySecureP@ssw0rd2024"]
    for pwd in test_passwords:
        print(f"  '{pwd}': {password_strength(pwd)}")

def main():
    try:
        print(generate_password())
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
