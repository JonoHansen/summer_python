# Guess the number game
import random
guessesTaken = 0

myName = raw_input("What is your name? >>")
number = random.randint(1,10)

print "I'm thinking of a number between 1 and 10."

while guessesTaken < 3:
    guess = raw_input("Guess what number >>")
    guess = int(guess)
    guessesTaken += 1 #this means guessesTaken + 1

    if guess < number:
        print "Too low, go higher."
    if guess > number:
        print "Too high, go lower."
    if guess == number:
        break 

if guess == number:
    print "Good job %s! You guessed it in %d times" % (myName,guessesTaken)
else:
    print "Too bad, I'm thinking of %s" %(number)
