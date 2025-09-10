import random

# ======== Word List & Welcome Message ========
print(r'''
Welcome to Cognitive Word Puzzle!
  ____                     _                ___                  _
 / ___|_   _  ___  ___ ___(_)_ __   __ _   / _ \ _   _  ___  ___| |_
| |  _| | | |/ _ \/ __/ __| | '_ \ / _` | | | | | | | |/ _ \/ __| __|
| |_| | |_| |  __/\__ \__ \ | | | | (_| | | |_| | |_| |  __/\__ \ |_
 \____|\__,_|\___||___/___/_|_| |_|\__, |  \__\_\\__,_|\___||___/\__|
                                   |___/
Getting word...
''')

WORD_LIST = [
    'apple','alias','alloy','banana','bongo','bogey','blueberry',
    'category','chains','grapes','orange','strawberry'
]

MAX_MISSES = 6  # maximum allowed wrong guesses


# ======== Secret Word Management ========
def get_secret_word(word_list):
    """Selects a random word and returns it in uppercase along with the initial display string."""
    secret = random.choice(word_list).upper()
    display_string = "_" * len(secret)
    return secret, display_string


# ======== Input Validation ========
def get_user_guess(previous_guesses):
    """Prompts user for a single letter guess, validates input, and prevents duplicates."""
    while True:
        guess = input("Guess a letter: ").strip().upper()
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single alphabetic character.")
        elif guess in previous_guesses:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter.")
        else:
            return guess


# ======== Display Update ========
def update_display(secret, display_string, guess):
    """Updates the display string based on the user's guess."""
    new_display = list(display_string)
    hit = False
    for i, ch in enumerate(secret):
        if guess == ch:
            new_display[i] = ch
            hit = True
    return "".join(new_display), hit


def show_state(display_string, missed_guesses, previous_guesses):
    """Displays the current word, missed guesses, and guessed letters."""
    print("\nWord: ", " ".join(display_string))
    print(f"Missed guesses: {missed_guesses}/{MAX_MISSES}")
    print(f"Guessed letters: {', '.join(sorted(previous_guesses))}\n")


# ======== Main Game Logic ========
def play_game():
    secret, display_string = get_secret_word(WORD_LIST)
    missed_guesses = 0
    previous_guesses = set()
    total_guesses = 0

    while display_string != secret and missed_guesses < MAX_MISSES:
        show_state(display_string, missed_guesses, previous_guesses)
        guess = get_user_guess(previous_guesses)
        previous_guesses.add(guess)
        total_guesses += 1

        display_string, hit = update_display(secret, display_string, guess)
        if not hit:
            missed_guesses += 1
            print(f"❌ '{guess}' is not in the word!")

    # ======== Game Over Messages ========
    show_state(display_string, missed_guesses, previous_guesses)
    if display_string == secret:
        print(f"🎉 Correct! The word was '{secret}'. Solved in {total_guesses} guesses!")
    else:
        print(f"💀 Game Over! The word was '{secret}'.")


# ======== Replay Option ========
def main():
    while True:
        play_game()
        replay = input("\nDo you want to play again? (Y/N): ").strip().upper()
        if replay != 'Y':
            print("Thanks for playing Cognitive Word Puzzle! Goodbye!")
            break


if __name__ == "__main__":
    main()
