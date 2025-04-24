# https://danielwilczak101.medium.com/control-a-stepper-motor-using-python-and-a-raspberry-pi-11f67d5a8d6d
from gpiozero import OutputDevice
from time import sleep

# Define the GPIO pins
dir_pin = "GPIO13"      # Direction pin
pulse_pin = "GPIO19"    # Pulse pin

# enable_pin = 26   # Enable pin

# Initialize the pins as output devices
pulse = OutputDevice(pulse_pin, active_high=True)
direction = OutputDevice(dir_pin, active_high=True)  # Active high to rotate CW
# enable = OutputDevice(enable_pin, active_high=False)  # Active low to enable the driver

# Enable the driver (this must be done to activate the TB6600)
# enable.on()
# sleep(0.5)  # Small delay to allow the driver to initialize

# Direction values (1 for CCW, 0 for CW)
ccw_direction_2 = 1
cw_direction_2 = 0

def set_direction(direction_value):
    """
    Sets the direction of the motor.
    - direction_value should be ccw_direction_2 (1) for CCW
    - direction_value should be cw_direction_2 (0) for CW
    """
    direction.value = direction_value  # Set the direction pin based on the value (0 or 1)
    if direction_value == cw_direction_2:
        print("Direction: CW (Active Low)")
    else:
        print("Direction: CCW (Active High)")

def step(steps=1, delay=0.0001):  # Adjust pulse delay as needed
    for _ in range(steps):
        pulse.on()  # Send pulse to TB6600
        sleep(delay)
        pulse.off()
        sleep(delay)

# Test the movement with CW (Clockwise)
print("Starting CW rotation...")
set_direction(cw_direction_2)  # Set direction to CW (0)
step(steps=2000, delay=0.0005)  # Execute 200 steps with 1ms delay

sleep(1)  # Pause for a moment

# Test the movement with CCW (Counter-Clockwise)
print("Starting CCW rotation...")
set_direction(ccw_direction_2)  # Set direction to CCW (1)
step(steps=2000, delay=0.0005)  # Execute 200 steps with 1ms delay

print("Test complete.")