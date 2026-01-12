#!/usr/bin/env python3
"""
Number Guessing Game Script
A simple game where the player tries to guess a random number.
"""

import random

def play_game(min_num=1, max_num=100, max_attempts=10):
    """
    Play a number guessing game.
    
    Args:
        min_num (int): Minimum number in range
        max_num (int): Maximum number in range
        max_attempts (int): Maximum number of attempts allowed
    
    Returns:
        bool: True if player won, False otherwise
    """
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    
    print(f"Guess a number between {min_num} and {max_num}")
    print(f"You have {max_attempts} attempts")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                return True
        except ValueError:
            print("Please enter a valid number")
            continue
    
    print(f"\nGame Over! The number was {secret_number}")
    return False

def main():
    """Main function to start the game."""
    print("=== Number Guessing Game ===\n")
    play_game()

def main():
    try:
        print(play_game())
    except Exception as exc:
        print(exc)

if __name__ == "__main__":
    main()
