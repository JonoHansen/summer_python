from sys import exit
import random

def start():
    print "You are stranded on an island after a fatal plane crash."
    print "The nearest hint of civilization is 100 miles away."
    print "Being the only survivor from the crash, you are on your own."
    print "Would you like to search for resources or wait for help?"
    choice = raw_input("search/wait >>").upper()
    if "WAIT" in choice:
        dead("Too bad, no one comes to your aid. You starve to death. Game over.")
    elif "SEARCH" in choice:
        print "Would you like to venture into the jungle or check the beach?"
        place = raw_input("jungle/beach >>").upper()
        if "JUNGLE" in place:
            jungle()
        elif "BEACH" in place:
            beach()
    else:
        dead("You failed to make a reasonable choice. Only the logical can survive in such a situation. Game over.")

def beach():
    print "Water is raging along the shore. Unknown creatures may lurk in the water."
    print "The sand under your feet feels as if its sucking you in."
    print "Do you explore the sea or the sand?"
    choice = raw_input("sea/sand >>").upper()
    if "SEA" in choice:
        print ""
        dead("A killer whale came out of nowhere and gulped you up. Game over.")
    elif "SAND" in choice:
        dead("The sand starts shaking vigorously. A sandcrawler pops out behind you and rips off your head. Game over.")

def jungle():
    print "Skyscraping trees loom over your head. They offer you fruits of vibrant colors."
    print "However, at the corner of your eye, you catch a glimpse of a golden monument."
    print "It seems to be a mysterious temple..."
    print "Where would you like to explore?"
    choice = raw_input("trees/temple >>").upper()
    if "TREES" in choice:
        print "You spot some purple and green fruits dangling from the trees."
        print "Which one will you choose to fill your stomach?"
        color = raw_input("green/purple >>").upper()
        if "GREEN" in color:
            green_fruit()
        elif "PURPLE" in color:
            dead("Oh no, the friut is poisonous. Game over.")
    elif "TEMPLE" in choice:
        print "You arrive at the temple. Two doors await you. Do you choose the left or the right one?"
        door = raw_input("left/right >>").upper()
        if "LEFT" in door:
            print "You open the left door."
            print "You see plates of food."
            print "Do you eat them or go to the door on the right instead?"
            food = raw_input("eat/change door >>").upper()
            if "EAT" in food:
                win("Congratulations! You made a logical decision.")
                win("You successfully fed yourself full and survived day 1.")
                win("Don't be too excited! Your adventure has just started...")
                exit(0)
            elif food == "CHANGE DOOR":
                door_right()
        elif door == "RIGHT":
            door_right()

def green_fruit():
    print "You take a bite out of the fruit."
    print '"Hmmm... It tastes delicious!! I shall eat some more." you say out loud.'
    win("Congratulations! You successfully fed yourself full and survived day 1.")
    win("Don't be too excited! Your adventure has just started...")
    exit(0)

def door_right():
    print "You open the right door."
    print "An ancient guardian knight stands in your way."
    print "Do you choose to reason with him, fight with him or flee?"
    choice = raw_input ("reason / fight / flee >>")
    if choice == "flee":
        jungle()
    elif choice == "fight":
        dead("Sorry. Your bare hands are no match for a spear and a shield. Game over.")
    elif choice == "reason":
        print "You explain to the guardian about what you want."
        print "He promises he will give you food and shelter if you guess the number he's thinking."
        print "Do you want to play the guardain's game?"
        game = raw_input ("yes / no, I'll leave the temple >>").upper()
        if "YES" in game:
            print "The guardian is thinking of a number between 1 and 10"
            print "He offers you 3 chances to guess his number."
            guessesTaken = 0
            number = random.randint(1,10)
            while guessesTaken < 3:
                guess = raw_input("Guess his number >>")
                guess = int(guess)
                guessesTaken += 1 #this means guessesTaken + 1

                if guess < number:
                    print "Too low, go higher."
                if guess > number:
                    print "Too high, go lower."
                if guess == number:
                    break

            if guess == number:
                print "There you go! You guessed correctly!"
                win("You are given a luxurious meal and shelter.")
                win("You successfully fed yourself full and survived day 1.")
                win("Don't be too excited! Your adventure has just started...")
                exit(0)
            elif guess != number:
                dead("Too bad, you fail to outwit the guardian. He kills you with his sword. Game over.")

        elif "NO" or "LEAVE" in game:
            jungle()


def win(msg):
    print msg

def dead(msg):
    print msg
    exit(0)

start()
