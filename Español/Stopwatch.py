# -*- coding: utf-8 -*-

import time
print "Cron�metro en funcionamiento. Pulse Control + C para detener el cron�metro. El cron�metro s�lo cuenta en segundos."

x = 0
while x > -1:
    print x
    time.sleep(1.00)
    x = x+1
