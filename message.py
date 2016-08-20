import random
import time
print "Welcome to fake message. Please note, this program is intended for entertainment purposes only. You will not talk with any real person, nothing is also sent to any server. Phone numbers are also fake, do not try to call or text the numbers that are randomly generated. This message will disappear in 15 seconds..."
time.sleep(15.00)
x = 80
while x > 0:
    print ""
    x = x-1

time.sleep(3.00)
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
print "So what do yyou want to talk about?"
m()
print "Cool."
m()
print "Nice"
m()
print "Talk later> Need to go."
x = 0
while x == 0:
    #m()
    #print "No internet. Make sure that you are connected to the Internet, then try again."
    print "Other person disconnected from server."