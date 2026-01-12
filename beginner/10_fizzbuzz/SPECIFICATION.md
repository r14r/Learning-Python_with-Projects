# Pflichtenheft: FizzBuzz

## Expected Functionality
Classic FizzBuzz implementation that replaces numbers divisible by 3 with "Fizz", numbers divisible by 5 with "Buzz", and numbers divisible by both with "FizzBuzz".

## Input
- **Function parameter**: `n` (integer) - The number to evaluate
- **Range parameters**: `start` and `end` for generating sequences

## Expected Output
```
FizzBuzz Demo (1-30)
1: 1
2: 2
3: Fizz
4: 4
5: Buzz
6: Fizz
7: 7
8: 8
9: Fizz
10: Buzz
11: 11
12: Fizz
13: 13
14: 14
15: FizzBuzz
...
30: FizzBuzz
```

## Tests

### Test 1: Divisible by 3
**Input:** `fizzbuzz(9)`  
**Expected Output:** `"Fizz"`

### Test 2: Divisible by 5
**Input:** `fizzbuzz(10)`  
**Expected Output:** `"Buzz"`

### Test 3: Divisible by Both 3 and 5
**Input:** `fizzbuzz(15)`  
**Expected Output:** `"FizzBuzz"`

### Test 4: Not Divisible by 3 or 5
**Input:** `fizzbuzz(7)`  
**Expected Output:** `7`

### Test 5: Range Generation
**Input:** `fizzbuzz_range(1, 5)`  
**Expected Output:** `[1, 2, "Fizz", 4, "Buzz"]`

## Usage
```bash
python script.py
```
