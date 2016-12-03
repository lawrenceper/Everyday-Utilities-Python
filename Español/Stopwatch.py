import time
print "Stopwatch running. Press Control+C to stop the stopwatch. The stopwatch only counts in seconds."

x = 0
while x > -1:
    print x
    time.sleep(1.00)
    x = x+1
