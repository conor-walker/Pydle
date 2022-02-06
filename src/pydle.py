import os
import random
import sys
from datetime import date

from colorama import init, Fore


def add_colour(colour, uncoloured_string):
    return colour + uncoloured_string + Fore.RESET


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
    return "".join(word_to_guess) == str(word_guessed).upper()


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
    print(add_colour(Fore.MAGENTA, header()))
    print("A totally original guessing game!")


def game_over(user_was_right, correct_word):
    if user_was_right:
        print("Congratulations! You figured it out!")
    else:
        print("Ran out of guesses! The word was:", add_colour(Fore.GREEN, ''.join(correct_word).capitalize()))
    input("Thanks for playing! Press ENTER to exit :)")
    sys.exit(0)


def count_letter_frequency(word):
    letter_frequency = {}
    for letter in word:
        letter_frequency[letter] = letter_frequency[letter] + 1 if letter in letter_frequency else 1
    return letter_frequency


def initialise_letter_frequency(word):
    letter_frequency = {}
    for letter in word:
        letter_frequency[letter] = 0
    return letter_frequency


def get_wordle_string(users_guess_input, word_to_be_guessed):
    green_letters = count_letter_frequency(word_to_be_guessed)
    yellow_letters = initialise_letter_frequency(word_to_be_guessed)
    wordle_string = []

    for index, letter in enumerate(users_guess_input):
        if word_to_be_guessed[index] == letter:
            green_letters[letter] = green_letters[letter] - 1
            wordle_string.append((Fore.GREEN, letter))
        else:
            wordle_string.append((Fore.LIGHTBLACK_EX, letter))

    for index, (colour, letter) in enumerate(wordle_string):
        if letter in word_to_be_guessed and yellow_letters[letter] < green_letters[letter] and colour != Fore.GREEN:
            yellow_letters[letter] = yellow_letters[letter] + 1
            wordle_string[index] = (Fore.YELLOW, letter)

    return " ".join([add_colour(colour, letter) for colour, letter in wordle_string])


# Main game flow.
def game_logic():
    word_to_be_guessed = list(get_random_word().upper())
    counter = 1
    while counter < 7:
        users_guess_input = get_guess(counter)
        print("Result:", get_wordle_string(users_guess_input, word_to_be_guessed))
        if check_word_is_right(word_to_be_guessed, users_guess_input):
            game_over(True, word_to_be_guessed)
        counter += 1
    game_over(False, word_to_be_guessed)


def main():
    intro()
    game_logic()


if __name__ == '__main__':
    init()
    main()
