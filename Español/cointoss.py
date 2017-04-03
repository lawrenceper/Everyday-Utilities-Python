import random
import time
print "Welcome to Coin Toss."
automode = raw_input("Would you like the automatic mode? Automatic mode allows you to watch, or listen, to your computer while you do other things. You'll not be prompted to press enter to flip the coin. Type Y to enable, and N to disable.")

#while automode != ("y", "n"):
#    print "Invalid Command."
#    automode = raw_input("Would you like the automatic mode? Automatic mode allows you to watch, or listen, to your computer while you do other things. You'll not be prompted to press enter to flip the coin. Type Y to enable, and N to disable.")

if automode == "y":
    print "Enabled."

while automode == "y":
    time.sleep (5.00)
    print "Flipped."
    time.sleep(2.50)
    a = random.randint(1,2)
    if a == 1:
        print "Lands face-up."

    if a == 2:
        print "Lands Face-down."



if automode == "n":
    print "Disabled."

while automode == "n":
    time.sleep(1.00)
    input=raw_input("Press enter to flip.")
    print "Flipped."
    time.sleep(2.50)
    a = random.randint
    if a == 1:
        print "Lands face-up."

    if a == 2:
        print "Lands Face-down."


