from sys import exit

# declare a function called "start"
def start():
    print "You fell into a deep cave."
    print "In front of you are two tunnels."
    print "Are you taking the left one or the right one?"
    choice = raw_input("left / right >>")
    if choice == "left":
        coffin_room()
    elif choice == "right":
        mummy_room()
    else:
        print "You stay in the same spot and starve to death. Game over."


def coffin_room():
    print "There is a coffin."
    print "Ancient symbols are written on the surface of it."
    print "What are you going to do with it?"
    coffin_opened = False

    # Write a while loop that repeats forever unless we run dead() or gold_room(). There will be three options - take away / yell / touch the symbols. PLayers must first touch the words before opening the coffin. All other options lead to death.
    while True: #forever
        choice = raw_input("take it away / open the coffin / touch the symbols >>")
        if choice == "take it away":
            dead("A trap is triggered. Swords fall onto you. Game over.")
        elif choice == "touch the symbols" and not coffin_opened:
            #coffin_opened==false
            print "The coffin shaked."
            coffin_opened = True
        elif choice == "touch the symbols" and coffin_opened:
            dead("You are possessed by a demon. Game over.")
        elif choice == "open the coffin" and not coffin_opened:
            dead("Your hand is stuck to the lock. Game over.")
        elif choice == "open the coffin" and coffin_opened:
            gold_room()
        else:
            print "Please choose one of the following:"

def mummy_room():
    print "A withered mummy is walking around searching for food."
    print "If it spots you, you'll be its meal."
    print "Do you flee or fight the beast?"
    choice = raw_input("flee / fight>>")
    if  "flee" in choice:
        start()
    elif "fight" in choice:
        dead("The mummy feasts on your brain. You become an undead too. Game over.")
    else:
        print "You feel the mummy's gaze over you..."
        mummy_room()

def gold_room():
    print "The coffin is full of gold!"
    print "How much do you take?"
    choice = raw_input("Type a number >>")
    choice = int(choice)

    if choice < 100:
        print "Good job! You are not greedy! You are whisked back to your home safely."
        exit(0)
    else:
        dead("You are too greedy! You get stuck in the room. Game over.")

def dead(msg):
    print msg
    exit(0)
# write a conditional that calls bear_room() if we turn left, and cthulhu_room()if right

start()
