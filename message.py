import random
import time
print "Welcome to fake message. Please note, this program is intended for entertainment purposes only. You will not talk with any real person, nothing is also sent to any server. Phone numbers are also fake, do not try to call or text the numbers that are randomly generated. This message will disappear in 15 seconds..."
time.sleep(15.00)
x = 80
while x > 0:
    print ""
    x = x-1

time.sleep(5.00)
a = random.randint(0,9)
b = random.randint(0,9)
c = random.randint(0,9)
d = random.randint(0,9)
e = random.randint(0,9)
f = random.randint(0,9)
g = random.randint(0,9)
h = random.randint(0,9)
i = random.randint(0,9)
j = random.randint(0,9)


print (("You have a message from "), (a), (b), (c), ("-"), (d), (e), (f), ("-"), (g), (h), (i), (j), (". It says, Hi."))
def m():
    message = raw_input("Type a message...")
    print "Sending..."
    time.sleep(1.5)
    print "Sent."
    time.sleep(10.00)



m()
print "Doing good. You?"
m()
print "Totally Awesome."
m()
print "LOL. Me too. :-) "
m()
print "That is really interesting. How did you do that?"
m()
print "I want to learn computer programming too. Some day, when you have the chance, can you teach me?"
m()
print "I think that yu might need to get a fast computer for that, which is something that I don't have. My PC has a 4 Megahurts processer and 2 bytes of RAM. It can connect to the Internet, but it takes over 200 years to load a webpage."
m()
print "I do not have the money for a new one. Mine is the 1960's brand. I have to stick cards into it, in order for it to read my code."
m()
print "Yes. But if I don't know programming, how can I use the computer? What can I do? It's powered off. When I power it on, it prints a whole lot of messages. Like over 1000 of them. It's a waist of paper. So what can I do?"
x = 0
while x == 0:
    m()
    print "No internet. Make sure that you are connected to the Internet, then try again."