from gpiozero import LED
from time import sleep

led = LED(17)  # Use GPIO17 (Pin 11)

stop = 0.25

while True:
    led.on()   # LED on
    sleep(stop)
    led.off()  # LED off
    sleep(stop)