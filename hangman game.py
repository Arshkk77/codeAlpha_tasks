#hangman game
import random

# List of words
word_list = ["python", "hangman", "developer", "computer", "keyboard", "programming"]

# Select a random word
word = random.choice(word_list).lower()
word_display = ["_"] * len(word)
attempts = 6  # Maximum incorrect attempts allowed
guessed_letters = set()

print("Welcome to Hangman!")

while attempts > 0 and "_" in word_display:
    print("\nWord:", " ".join(word_display))
    print(f"Incorrect attempts left: {attempts}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter. Try a different one.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        print("Good job! Letter found.")
        for i, letter in enumerate(word):
            if letter == guess:
                word_display[i] = guess
    else:
        print("Oops! Wrong guess.")
        attempts -= 1

if "_" not in word_display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The correct word was:", word)

