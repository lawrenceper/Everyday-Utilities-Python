import random
import time
print "Welcome to the spinning game."
x = 0
while x == 0:
    i = raw_input("Press enter to spin.")
    sleeptime = 0.04
    while sleeptime < 0.3:
        print ("Spinning")
        time.sleep(sleeptime)
        sleeptime += 0.02

    while sleeptime < 0.5:
        print "Spinning"
        time.sleep(sleeptime)
        sleeptime += 0.05
    while sleeptime < 1.00:
        print "Spinning"
        time.sleep(sleeptime)
        sleeptime += 0.25

    a = (random.randint(0,16))
    if a == 0:
        print "The spinner keeps spinning. It flew off the board and it's moving very fasleeptime... To the edge of the table! It hits the wall and falls on the floor with a loud bang. Your dog wakes up and sleeptimearts barking madly. You need to pick up the spinner before you can spin it again."
        pickup = raw_input('Type "pick up" to pick it up.')
        if pickup == "pick up":
            print "You pick it up."

        else:
            print "Invalid command."

    if a > 8:
        print "The spinner keeps spinning. It flew off the board and it's moving very fast... To the edge of the table! It hits the wall and falls on the floor with a loud bang. Your dog wakes up and starts barking madly. You need to pick up the spinner before you can spin it again."
        pickup = raw_input('Type "pick up" to pick it up.')
        if pickup == "pick up":
            print "You pick it up."


    else:
        print (a)

