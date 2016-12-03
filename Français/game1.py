#Imports modules.
import threading
import time
import random
#resets the number of guesses (g) variable.
g = 0
#Timer settings.
class Timer(threading.Thread):
    #Initial settings for timer
    def __init__(self, i=0.001):
        threading.Thread.__init__(self)
        self.i = i
        self.value = 0
        self.alive = False

    #When Running timer.
    def run(self):
        self.alive = True
        while self.alive:
            time.sleep(self.i)
            self.value += self.i

    #when timer stopps
    def finish(self):
        self.alive = False
        return self.value


timerun = Timer()
timerun.start()

#The variables for the random number and the input are named A and B, because Python wouldn't
#let me set rand and in variables, probably because something else is using the same name.
#Variable A is the random number, and variable B is the input.
print "Welcome to game 1."
#time .sleep is set here, to give the person who's reading it, or the screen reader, a chance to read the text that was printed on the screen.
time.sleep(3.00)
#Start new level. Time.sleep is used here to make it seem as if the computer is really thinking like a human, will be set longer per new level.
print "Level 1. Please wait. Thinking..."
time.sleep(3.00)
a = (random.randint (1,10))
b = (input("I'm thinking of a number between 1 and 10. What number am I thinking of? Type your answer in the terminal window or Python shell."))
while b != a:
    b = (input("Sorry, try again."))
    g = g+1

if b == a:
    print "You won this level."
    time.sleep(2.50)

print "Total guesses so far:"
print g
time.sleep(3.00)

#Start new level.
print "Level 2. Please wait. Thinking..."
time.sleep(5.00)
a = (random.randint (1,20))
b = (input("I'm thinking of a number between 1 and 20. What number am I thinking of?"))
while b != a:
    b = (input("Sorry, try again."))
    g = g+1

if b == a:
    print "You won this level."
    time.sleep(2.50)

print "Total guesses so far:"
print g
time.sleep(3.00)

#Start new level.
print "Level 3. Please wait. Thinking..."
time.sleep(7.50)
a = (random.randint (1,30))
b = (input("I'm thinking of a number between 1 and 30. What number am I thinking of?"))
while b != a:
    b = (input("Sorry, try again."))
    g = g+1

if b == a:
    print "You won this level."
    time.sleep(2.50)

print "Total guesses so far:"
print g
time.sleep(3.00)

#Prints a message.
print "Things are going to get a lot harder. Are you ready?"
time.sleep(4.00)
#Start new level.
print "Level 4. Please wait. Thinking..."
time.sleep(10.00)
a = (random.randint (1,50))
b = (input("I'm thinking of a number between 1 and 50. What number am I thinking of?"))
while b != a:
    b = (input("Sorry, try again."))
    g = g+1

if b == a:
    print "You won this level."
    time.sleep(2.50)

print "Total guesses so far:"
print g
time.sleep(3.00)

#Start new level.
print "Level 5. Please wait. Thinking..."
time.sleep(15.00)
a = (random.randint (1,20))
b = (input("I'm thinking of a number between 1 and 100. What number am I thinking of?"))
while b != a:
    b = (input("Sorry, try again."))
    g = g+1

if b == a:
    print "You won this level."
    time.sleep(2.50)

print "Total guesses so far:"
print g
time.sleep(3.00)

#Prints a message.
print "Much, much harder. Here we go."
time.sleep(3.00)

#Start new level.
print "Level 6. Please wait. Thinking..."
time.sleep(22.50)
a = (random.randint (1,500))
b = (input("I'm thinking of a number between 1 and 500. What number am I thinking of?"))
while b != a:
    b = (input("Sorry, try again."))
    g = g+1

if b == a:
    print "You won this level."
    time.sleep(2.50)

print "Total guesses so far:"
print g
time.sleep(3.00)

#Start new level.
print "Level 7. Please wait. Thinking..."
time.sleep(30.00)
a = (random.randint (1,1000))
b = (input("I'm thinking of a number between 1 and 1000. What number am I thinking of?"))
while b != a:
    b = (input("Sorry, try again."))
    g = g+1

if b == a:
    print "You won this level."
    time.sleep(2.50)

#Prints another message.
print "You won the game!"
time.sleep(2.30)
print "Total guesses:"
print g
time.sleep(3.00)

print "Thanks for playing."
print "You spent", timerun.finish(), "seconds."
