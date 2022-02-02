import os
import random
import sys
from datetime import date

from colorama import init, Fore


def add_colour(colour, uncoloured_string):  # I COULD NOT RESIST NAMING IT THIS I'M SORRY - Goudham
    return colour + uncoloured_string + Fore.RESET  # Add the given colour and then resets it - Goudham


# Gets the input from a user - number param is used to display the guess number the user is on
def get_guess(number):
    validGuess = False
    guess = ""
    while not validGuess:
        guess = str(input("Guess " + str(number) + " / 6: ")).upper()
        if len(guess) > 5 or len(guess) < 5:
            print("Invalid guess - please ensure you're guessing a word of 5 letters")
        else:
            validGuess = True
    return guess


# Get absolute path to resource - works when run from script and compiled using PyInstaller
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# Gets a random word from a words.txt file present in the same directory as this script.
# If file is not present, uses a small fallback list of words.
# Shuffles based on a seed and selects a consistent member of the list to allow consistency between runs on same day.
def get_random_word():
    try:
        lines = open(resource_path('words.txt')).read().splitlines()
    except IOError:
        lines = ["Arrow", "Pride", "Whole", "React", "Chose", "Quote", "Adieu", "Story", "Whale", "Musty", "Korea",
                 "Snide", "Zebra", "Shite", "Plans", "Bride", "Blare", "Child", "Towns", "Treat", "Lusty", "Ocean"]
    random.seed(int(date.today().day))
    random.shuffle(lines)
    return lines[1]


# Compares the users input with the word to be guessed. Returns true if the guess is correct, false otherwise
def check_word_is_right(word_to_guess, word_guessed):
    return "".join(word_to_guess) == str(word_guessed).upper()  # The 'word_to_guess' will now be a list - Goudham


# Makes a cool header.
def header():
    return r" ______   ______  _     _____" + "\n" + \
           r"|  _ \ \ / /  _ \| |   | ____|" + "\n" + \
           r"| |_) \ V /| | | | |   |  _|" + "\n" + \
           r"|  __/ | | | |_| | |___| |___" + "\n" + \
           r"|_|    |_| |____/|_____|_____|"


# Prints welcome messages
def intro():
    print("Welcome to...")
    print(add_colour(Fore.MAGENTA, header()))  # You could make this multicoloured - Goudham
    print("A totally original guessing game!")


# Prints the results, a thank-you message and gracefully exits
def game_over(user_was_right, correct_word):
    coloured_correct_word = add_colour(Fore.GREEN, ''.join(correct_word).capitalize())
    if user_was_right:
        print("Congratulations! The word was:", coloured_correct_word)
    else:
        print("Ran out of guesses! The word was:", coloured_correct_word)
    input("Thanks for playing! Press ENTER to exit :)")
    sys.exit(0)


# Takes in the users guess and the myriad lists involved in the game logic, and compares the letters in the guess
# with the word to be guessed.
# Inserts the letter into the appropriate list, based on its presence & position (or lack thereof)
# So this is like a massive rework right, it's basically like the actual wordle game with colouring - Goudham
def check_letter_in_word(users_guess_input, word_to_be_guessed, users_guess_results):
    correct = []
    for i in range(len(users_guess_input)):
        if word_to_be_guessed[i] == users_guess_input[i]:
            correct.append(users_guess_input[i])
            users_guess_results[i] = add_colour(Fore.GREEN, users_guess_input[i])
        elif users_guess_input[i:] in word_to_be_guessed and users_guess_input[i] not in correct:
            users_guess_results[i] = add_colour(Fore.YELLOW, users_guess_input[i])
        else:
            users_guess_results[i] = users_guess_input[i]


# Main game flow.
def game_logic():
    word_to_be_guessed = list(get_random_word().upper())
    counter = 1
    while counter < 7:
        users_guess_input = get_guess(counter)
        # You can check if the game is over right after the user enters the word - Goudham
        if check_word_is_right(word_to_be_guessed, users_guess_input):
            game_over(True, word_to_be_guessed)
        users_guess_results = ["_"] * 5
        check_letter_in_word(users_guess_input, word_to_be_guessed, users_guess_results)
        print("Result: " + " ".join(users_guess_results))
        counter += 1
    game_over(False, word_to_be_guessed)


def main():
    intro()
    game_logic()


if __name__ == '__main__':
    # I promise that this just started out with wanting to add colours... turned into a rework sorry :( - Goudham
    init()  # Read -> https://pypi.org/project/colorama/ - Goudham
    main()
