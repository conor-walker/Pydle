import random


def getGuess():
    validGuess = False
    guess = ""
    while not validGuess:
        guess = str(input("Please guess:")).upper()
        if len(guess) > 5 or len(guess) < 5:
            print("Invalid guess - please ensure you're guessing a word of 5 letters")
        else:
            validGuess = True
    return guess


def getWord():
    lines = open('words').read().splitlines()
    return random.choice(lines)


def checkRight(wordToGuess, guessSoFar):
    if str(wordToGuess).upper() == str(guessSoFar).upper():
        return True
    else:
        return False


emptyWordGuess = ["_"]*5
wrongLetters = set()
rightLettersWrongPlace = set()
wordToGuess = list(getWord().upper())
# print(wordToGuess)

counter = 0
while counter < 5:
    userGuess = getGuess()
    emptyWordGuess = ["_"]*5
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
    print("Incorrect letters: " + str(wrongLetters))
    print("Correct letters in the wrong place: " + str(rightLettersWrongPlace))
    print("Result: " + " ".join(emptyWordGuess))
    counter += 1

print("Ran out of guesses! The word was: ", "".join(wordToGuess))
exit(69)
