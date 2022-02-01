import os
import random
import sys


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


# Gets a random word from a words.txt file present in the same directory as this script
def get_random_word():
    lines = open(resource_path('words.txt')).read().splitlines()
    return random.choice(lines)


# Compares the users input with the word to be guessed. Returns true if the guess is correct, false otherwise
def check_word_is_right(word_guessed, word_to_guess):
    if str(word_guessed).upper() == str(word_to_guess).upper():
        return True
    else:
        return False


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
    print(header())
    print("A totally original guessing game!")


# Prints the results, a thank-you message and gracefully exits
def game_over(user_was_right, correct_word):
    if user_was_right:
        print("Congratulations! The word was", ''.join(correct_word).capitalize())
    else:
        print("Ran out of guesses! The word was: ", "".join(correct_word))
    input("Thanks for playing! Press ENTER to exit :)")
    sys.exit(0)


# Takes in the users guess and the myriad lists involved in the game logic, and compares the letters in the guess
# with the word to be guessed.
# Inserts the letter into the appropriate list, based on its presence & position (or lack thereof)
def check_letter_in_word(users_guess_input, word_to_be_guessed, users_guess_results, present_in_word, not_in_word):
    for i in range(len(users_guess_input)):
        if word_to_be_guessed[i] == users_guess_input[i]:
            users_guess_results[i] = users_guess_input[i]
        elif users_guess_input[i] in word_to_be_guessed:
            if users_guess_input[i] in users_guess_results and users_guess_input[i] not in word_to_be_guessed[i:]:
                break
            else:
                present_in_word.add(users_guess_input[i])
        else:
            not_in_word.add(users_guess_input[i])


# Main game flow.
def game_logic():
    not_in_word, present_in_word = set(), set()
    word_to_be_guessed = list(get_random_word().upper())
    counter = 1
    while counter < 7:
        users_guess_input = get_guess(counter)
        users_guess_results = ["_"] * 5
        check_letter_in_word(users_guess_input, word_to_be_guessed, users_guess_results, present_in_word, not_in_word)
        if check_word_is_right(word_to_be_guessed, users_guess_results):
            game_over(True, word_to_be_guessed)
        print("Incorrect letters: " + ', '.join(not_in_word))
        print("Correct letters in the wrong place: " + ', '.join(present_in_word))
        print("Result: " + " ".join(users_guess_results))
        counter += 1
    game_over(False, word_to_be_guessed)


def main():
    intro()
    game_logic()


if __name__ == '__main__':
    main()
