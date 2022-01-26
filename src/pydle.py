import os
import random
import sys


def getGuess(number):
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


def getWord():
    lines = open(resource_path('words.txt')).read().splitlines()
    return random.choice(lines)


def checkRight(wordToGuess, guessSoFar):
    if str(wordToGuess).upper() == str(guessSoFar).upper():
        return True
    else:
        return False


def header():
    return r" ______   ______  _     _____" + "\n" + \
           r"|  _ \ \ / /  _ \| |   | ____|" + "\n" + \
           r"| |_) \ V /| | | | |   |  _|" + "\n" + \
           r"|  __/ | | | |_| | |___| |___" + "\n" + \
           r"|_|    |_| |____/|_____|_____|"


print("Welcome to...")
print(header())
print("A totally original guessing game!")
emptyWordGuess = ["_"] * 5
wrongLetters = set()
rightLettersWrongPlace = set()
wordToGuess = list(getWord().upper())
# print(wordToGuess)

counter = 1
while counter < 6:
    userGuess = getGuess(counter)
    emptyWordGuess = ["_"] * 5
    for i in range(len(userGuess)):
        if wordToGuess[i] == userGuess[i]:
            emptyWordGuess[i] = userGuess[i]
        elif userGuess[i] in wordToGuess:
            if userGuess[i] in emptyWordGuess and userGuess[i] not in wordToGuess[i:]:
                break
            else:
                rightLettersWrongPlace.add(userGuess[i])
        else:
            wrongLetters.add(userGuess[i])
    if checkRight(wordToGuess, emptyWordGuess):
        print("Congratulations! The word was", ''.join(wordToGuess).capitalize())
        exit(420)
    print("Incorrect letters: " + ', '.join(wrongLetters))

    print("Correct letters in the wrong place: " + ', '.join(rightLettersWrongPlace))
    print("Result: " + " ".join(emptyWordGuess))
    counter += 1

print("Ran out of guesses! The word was: ", "".join(wordToGuess))
exit(69)
