#!/usr/bin/env python3
"""
Hello World Script
A simple script that prints a greeting message.
"""

def greet(name="World"):
    """
    Print a greeting message.
    
    Args:
        name (str): Name to greet (default: "World")
    
    Returns:
        str: The greeting message
    """
    message = f"Hello, {name}!"
    return message

def main():
    """Main function to demonstrate the greeting."""
    print(greet())
    print(greet("Python Learner"))

def main():
    try:
        print(greet())
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
