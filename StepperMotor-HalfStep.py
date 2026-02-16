from machine import Pin
import time
mag1 = Pin(12, Pin.OUT)
mag2 = Pin(25, Pin.OUT)
mag3 = Pin(4, Pin.OUT)
mag4 = Pin(18, Pin.OUT)
while True:
    mag1.value(1)
    mag2.value(1)
    mag3.value(0)
    mag4.value(0)
    time.sleep(0.01)
  
    mag1.value(0)
    mag2.value(1)
    mag3.value(0)
    mag4.value(0)
    time.sleep(0.01)
  
    mag1.value(0)
    mag2.value(1)
    mag3.value(1)
    mag4.value(0)
    time.sleep(0.01)
  
    mag1.value(0)
    mag2.value(0)
    mag3.value(1)
    mag4.value(0)
    time.sleep(0.01)
  
    mag1.value(0)
    mag2.value(0)
    mag3.value(1)
    mag4.value(1)
    time.sleep(0.01)
  
    mag1.value(0)
    mag2.value(0)
    mag3.value(0)
    mag4.value(1)
    time.sleep(0.01)
  
    mag1.value(1)
    mag2.value(0)
    mag3.value(0)
    mag4.value(1)
    time.sleep(0.01)
  
    mag1.value(1)
    mag2.value(0)
    mag3.value(0)
    mag4.value(0)
    time.sleep(0.01)

