# Let's make Hangman

import random

HANGMANPICS = ['''
 +---+
 |   |
     |
     |
     |
     |
=========''','''
 +---+
 |   |
 O   |
     |
     |
     |
=========''','''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========''','''
 +---+
 |   |
 O   |
 |\  |
     |
     |
=========''','''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''','''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''','''
 +---+
 |   |
 O   |
/|\  |
/ \   |
     |
=========''']

#method showing the picture, the incorrect guesses and current blanks
def displayBoard(HANGMANPICS, missedLetters, correctLetters, myWord):
    print(HANGMANPICS[len(missedLetters)])
    print("You've taken %d incorrect guesses." % len(missedLetters))
    #loop to print out all incorrect guesses
    for letter in missedLetters:
        print(letter)
    #variable to hold blanks
    blanks = '_' * len(myWord)
    #prints out any correct guesses inside our blanks
    for i in range(len(myWord)):
        if myWord[i] in correctLetters:
            blanks = blanks[:i] + myWord[i] + blanks[i+1:]
    print blanks

#method to get the user's input (the actual guessing of the letter)
def getGuess(alreadyGuessedLetters):
    while True:
        guess = raw_input("Guess a letter!")
        guess = guess.lower()
        if len(guess) != 1:
            print("Please guess one letter :S")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a letter >.<")
        elif guess in alreadyGuessedLetters:
            print("You already guessed that letter! >:( ")
        else:
            return guess

#method to generate a random word
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList.split()) - 1)
    return wordList.split()[wordIndex]

#setting up variables as inputs
words = "jazzed bopping jinx joke quiz shivving waxes grogginess faking"
print("Hey there, let's play hangman!")
myWord = getRandomWord(words)
gameOver = False
correctLetters = ""
missedLetters = ""

#main loop
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, myWord)
    guess = getGuess(correctLetters + missedLetters)

    #check for user's guess
    if guess in myWord:
        correctLetters = correctLetters + guess
        #check if player got all the letters
        win = True
        for i in range(len(myWord)):
            if myWord[i] not in correctLetters:
                win = False
                break
        if win:
            print("You've guessed the word!")
            gameOver = True
    #user guesses incorrect letter
    else:
        missedLetters = missedLetters + guess
        if (len(HANGMANPICS) - 1) == len(missedLetters):
            displayBoard(HANGMANPICS, missedLetters, correctLetters, myWord)
            print("You've lost! The word is %s." % myWord)
            gameOver = True

    if gameOver:
        answer = raw_input("Do you want to play again?")
        answer.lower()
        if answer == "yes":
            myWord = getRandomWord(words)
            gameOver = False;
            correctLetters = ""
            missedLetters = ""
        else:
            break
