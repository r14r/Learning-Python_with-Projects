#!/usr/bin/env python3
"""
FizzBuzz Script
Classic FizzBuzz implementation - prints numbers with special rules.
"""


def fizzbuzz(n):
    """
    Return FizzBuzz value for a number.
    
    Args:
        n (int): The number to evaluate
    
    Returns:
        str or int: "Fizz" if divisible by 3, "Buzz" if divisible by 5,
                    "FizzBuzz" if divisible by both, otherwise the number
    """
    if n % 15 == 0:  # Divisible by both 3 and 5
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n


def fizzbuzz_range(start, end):
    """
    Generate FizzBuzz sequence for a range.
    
    Args:
        start (int): Start of range (inclusive)
        end (int): End of range (inclusive)
    
    Returns:
        list: FizzBuzz values for the range
    """
    return [fizzbuzz(i) for i in range(start, end + 1)]


def main():
    """Main function to demonstrate FizzBuzz."""
    print("FizzBuzz Demo (1-30)")
    for i in range(1, 31):
        print(f"{i}: {fizzbuzz(i)}")


if __name__ == "__main__":
    main()
