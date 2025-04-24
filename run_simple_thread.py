# https://danielwilczak101.medium.com/control-a-stepper-motor-using-python-and-a-raspberry-pi-11f67d5a8d6d
from gpiozero import OutputDevice, LED
from time import sleep
import os
import glob
import time
from threading import Thread

## LED
led = LED(17)  # Use GPIO17 (Pin 11)
led.on()   # LED on

## Temperature reading
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        # time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f


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

# steps = 10000
delay = 0.00005 # much more faster
# delay = 0.0001 # more faster
# delay = 0.00025 # faster
# delay = 0.0005 # moderate
# delay = 0.001 # slower

def stepper_motor():
    while True:
        pulse.on()  # Send pulse to TB6600
        sleep(delay)
        pulse.off()
        sleep(delay)
    
def temp_sensor():
    while True:
        print("Motor temperature (C): ", read_temp()[0])	
        time.sleep(1)

t1 = Thread(target = stepper_motor)
t2 = Thread(target = temp_sensor)

t1.start()
t2.start()

# enable.off()


led.off()   # LED on
