from ascii_art import *
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]  

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")

def play_game():
    mistakes = 0
    guessed_letters = []
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # TODO: Build your game loop here.
    # For now, simply prompt the user once:
    while True:
        if mistakes == len(STAGES) - 1:
            print(f"Game Over! The word was: {secret_word}")
            print()
            print(STAGES[mistakes])
            return
        else:
            display_game_state(mistakes, secret_word, guessed_letters)
            guess = input("Guess a letter: ").lower()
            print("You guessed:", guess)
            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue
            elif guess in secret_word:
                guessed_letters.append(guess)
                continue
            else:
                mistakes += 1



