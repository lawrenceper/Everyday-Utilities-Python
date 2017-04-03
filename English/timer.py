import time
print("Welcome to Open Timer.")
x = 0
while x == 0:
    sec = input("Enter the number of seconds.")
    while sec > 0:
        print (sec)
        time.sleep (1.00)
        sec = sec-1

    print (0)
    print("Timer Done.")
    time.sleep(3.00)

