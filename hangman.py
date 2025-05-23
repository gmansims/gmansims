import random

# List of words for the game. Feel free to expand this list with more common words.
WORD_LIST = [
    "python", "computer", "hangman", "challenge", "programming",
    "assistant", "openai", "github", "developer", "algorithm",
    "function", "variable", "condition", "iteration", "object",
    "inheritance", "exception", "compilation", "interpreter", "terminal"
]

HANGMAN_PICS = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =======
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =======
    """
]

MAX_ATTEMPTS = len(HANGMAN_PICS) - 1


def choose_word():
    """Select a random word from WORD_LIST."""
    return random.choice(WORD_LIST)


def display_board(hangman_state, guessed_word, guessed_letters):
    """Print the current hangman state and the word progress."""
    print(HANGMAN_PICS[hangman_state])
    print("Word:", " ".join(guessed_word))
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print()


def play_game():
    word = choose_word()
    guessed_letters = set()
    guessed_word = ["_" for _ in word]
    attempts = 0

    print("Let's play Hangman!")
    while attempts < MAX_ATTEMPTS and "_" in guessed_word:
        display_board(attempts, guessed_word, guessed_letters)
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.\n")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.add(guess)
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts += 1
            print(f"Incorrect! You have {MAX_ATTEMPTS - attempts} attempts left.\n")

    display_board(attempts, guessed_word, guessed_letters)
    if "_" not in guessed_word:
        print("Congratulations! You've guessed the word!")
    else:
        print(f"Sorry, you lost. The word was '{word}'.")


if __name__ == "__main__":
    play_game()
