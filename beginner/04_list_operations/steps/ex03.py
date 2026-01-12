#!/usr/bin/env python3
"""
List Operations Script
Demonstrates basic list operations and manipulations.
"""

def find_max(numbers):
    """Find the maximum number in a list."""
    if not numbers:
        return None
    return max(numbers)

def find_min(numbers):
    """Find the minimum number in a list."""
    if not numbers:
        return None
    return min(numbers)

def main():
    try:
        print(find_max("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
