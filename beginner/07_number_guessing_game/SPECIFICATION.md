# Pflichtenheft: Number Guessing Game

## Expected Functionality
A simple interactive game where the player tries to guess a randomly generated number within a specified range. The game provides feedback (too high/too low) and limits the number of attempts.

## Input
- **User input**: Integer guess from stdin
- **Function parameters**:
  - `min_num` (int, default: 1): Minimum number in range
  - `max_num` (int, default: 100): Maximum number in range
  - `max_attempts` (int, default: 10): Maximum attempts allowed

## Expected Output
Example game session:
```
=== Number Guessing Game ===

Guess a number between 1 and 100
You have 10 attempts

Attempt 1/10: 50
Too low!

Attempt 2/10: 75
Too high!

Attempt 3/10: 63
Congratulations! You guessed it in 3 attempts!
```

## Tests

### Test 1: Correct Guess on First Try
**Input:** User guesses the secret number immediately  
**Expected Output:** Success message with "1 attempts"

### Test 2: Too Low Feedback
**Input:** User guess < secret number  
**Expected Output:** "Too low!" message

### Test 3: Too High Feedback
**Input:** User guess > secret number  
**Expected Output:** "Too high!" message

### Test 4: Invalid Input
**Input:** User enters non-numeric value  
**Expected Output:** "Please enter a valid number" and attempt doesn't count

### Test 5: Max Attempts Reached
**Input:** 10 incorrect guesses  
**Expected Output:** "Game Over! The number was X" message

## Usage
```bash
python script.py
```
