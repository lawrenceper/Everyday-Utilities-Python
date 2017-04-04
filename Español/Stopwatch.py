# -*- coding: utf-8 -*-

import time
print "Cronómetro en funcionamiento. Pulse Control + C para detener el cronómetro. El cronómetro sólo cuenta en segundos."

x = 0
while x > -1:
    print x
    time.sleep(1.00)
    x = x+1
