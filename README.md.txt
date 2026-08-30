# CodeAlpha_Hangman 🎮

## Python Programming Internship — CodeAlpha
**Task 1: Hangman Game**

A simple text-based Hangman game built in Python. The player tries to guess a
hidden word one letter at a time before running out of allowed wrong guesses.

## Features
- 5 predefined words, chosen at random each game
- Maximum of 6 incorrect guesses allowed
- ASCII-art hangman figure that updates with each wrong guess
- Input validation (rejects repeated guesses, non-letters, multi-character input)
- Option to play again after each round

## Key Concepts Used
- `random` module
- `while` loops
- `if-else` conditionals
- Strings and lists
- Sets (to track guessed letters)

## How to Run
```bash
python3 hangman.py
```

## Example Gameplay
```
========================================
WELCOME TO HANGMAN
========================================
Try to guess the word. You have 6 wrong guesses allowed.

Word: _ _ _ _ _ _
Guessed letters: (none)
Wrong guesses: 0/6

Guess a letter: p
Good guess! 'p' is in the word.
```

## Author
Submitted as part of the CodeAlpha Python Programming Internship.

## About CodeAlpha
CodeAlpha is a software development company offering internship programs in
Python, Web Development, Data Science, and more. Learn more at
[www.codealpha.tech](https://www.codealpha.tech).
