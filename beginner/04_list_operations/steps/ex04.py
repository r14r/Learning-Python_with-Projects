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

def calculate_average(numbers):
    """Calculate the average of numbers in a list."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def remove_duplicates(items):
    """Remove duplicates from a list while preserving order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def main():
    try:
        print(find_max("demo"))
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
