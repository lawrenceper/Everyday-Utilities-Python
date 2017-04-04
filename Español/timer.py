# -*- coding: utf-8 -*-

import time
print("Bienvenido a Timer.")
x = 0
while x == 0:
    sec = input("Introduzca el número de segundos.")
    while sec > 0:
        print(sec)
        time.sleep (1.00)
        sec = sec-1

    print (0)
    print("Temporizador Hecho.")
    time.sleep(3.00)

