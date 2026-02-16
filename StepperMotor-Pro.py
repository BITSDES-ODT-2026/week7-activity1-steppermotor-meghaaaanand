from machine import Pin
import time
mag1 = Pin(12, Pin.OUT)
mag2 = Pin(25, Pin.OUT)
mag3 = Pin(4, Pin.OUT)
mag4 = Pin(18, Pin.OUT)
list1 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
list2 = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
while True:
    for i in range(1,500):
        for k in list1:
            mag1.value(k[0])
            mag2.value(k[1])
            mag3.value(k[2])
            mag4.value(k[3])
            time.sleep(0.003)
    for i in range (1,500):
        for k in list2:
            mag1.value(k[0])
            mag2.value(k[1])
            mag3.value(k[2])
            mag4.value(k[3])
            time.sleep(0.003)
