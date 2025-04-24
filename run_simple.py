# https://danielwilczak101.medium.com/control-a-stepper-motor-using-python-and-a-raspberry-pi-11f67d5a8d6d
from gpiozero import OutputDevice, LED
from time import sleep
import os
import glob
import time

## LED
led = LED(17)  # Use GPIO17 (Pin 11)
led.on()   # LED on

## Driving the stepper motor
# Define the GPIO pins
en_pin = "GPIO6"      # Enable pin
dir_pin = "GPIO13"      # Direction pin
pulse_pin = "GPIO19"    # Pulse pin

# Initialize the pins as output devices
pulse = OutputDevice(pulse_pin, active_high=True)
direction = OutputDevice(dir_pin, active_high=True)  # Active high to rotate CW
enable = OutputDevice(en_pin, active_high=True)
# enable.on()
print(enable.value)


# Direction values (1 for CCW, 0 for CW)
ccw_direction_2 = 1
cw_direction_2 = 0

direction.value = cw_direction_2
direction.value = ccw_direction_2

# Test the movement with CW (Clockwise)
print("Starting CW rotation...")

## microstep 4
# steps = 10000
# delay = 0.00005 # much more faster
# delay = 0.0001 # more faster
# delay = 0.00025 # faster
# delay = 0.0005 # moderate
# delay = 0.001 # slower

# microstep 2
# steps = 10000
# delay = 0.00005 # much more faster
# delay = 0.0001 # more faster
delay = 0.0002 # faster
# delay = 0.0005 # moderate
# delay = 0.001 # slower

# for _ in range(steps):
#     pulse.on()  # Send pulse to TB6600
#     sleep(delay)
#     pulse.off()
#     sleep(delay)





while True:
    pulse.on()  # Send pulse to TB6600
    sleep(delay)
    pulse.off()
    sleep(delay)
    

# enable.off()


led.off()   # LED on
