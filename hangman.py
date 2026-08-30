"""
CodeAlpha Python Programming Internship
Task 1: Hangman Game

A simple text-based Hangman game where the player guesses a word
one letter at a time.

Key Concepts Used: random, while loop, if-else, strings, lists.
"""

import random

WORDS = ["python", "hangman", "internship", "keyboard", "elephant"]
MAX_WRONG_GUESSES = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ----------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ----------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ----------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ----------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ----------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ----------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ----------
    """,
]


def choose_word():
    """Pick a random word from the predefined word list."""
    return random.choice(WORDS)


def display_state(word, guessed_letters, wrong_guesses):
    """Print the hangman figure, masked word, and guessed letters."""
    print(HANGMAN_STAGES[wrong_guesses])

    masked = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print("Word: " + masked)
    print("Guessed letters: " + ", ".join(sorted(guessed_letters)) if guessed_letters else "Guessed letters: (none)")
    print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}\n")


def get_guess(guessed_letters):
    """Prompt the user for a single, unused letter and validate the input."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try another.\n")
            continue

        return guess


def play_game():
    """Run a single round of Hangman."""
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("=" * 40)
    print("WELCOME TO HANGMAN")
    print("=" * 40)
    print(f"Try to guess the word. You have {MAX_WRONG_GUESSES} wrong guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        display_state(word, guessed_letters, wrong_guesses)

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"🎉 Congratulations! You guessed the word: '{word}'")
            return

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    # If loop exits, player has run out of guesses
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"💀 Game over! You ran out of guesses. The word was: '{word}'")


def main():
    play_again = "y"
    while play_again == "y":
        play_game()
        play_again = input("\nPlay again? (y/n): ").strip().lower()

    print("\nThanks for playing Hangman! Goodbye.")


if __name__ == "__main__":
    main()
