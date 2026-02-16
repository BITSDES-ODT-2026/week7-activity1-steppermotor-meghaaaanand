from machine import Pin
import time
mag1 = Pin(12, Pin.OUT)
mag2 = Pin(25, Pin.OUT)
mag3 = Pin(4, Pin.OUT)
mag4 = Pin(18, Pin.OUT)
list = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
while True:
    for i in list:
        mag1.value(i[0])
        mag2.value(i[1])
        mag3.value(i[2])
        mag4.value(i[3])
        time.sleep(0.005)
