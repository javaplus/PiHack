import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

def setUpBoard():
    GPIO.setwarnings(False)    # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # Set pin 10 to be an input pin and set initial value to low (off)

def isButtonDown(button_pin):
    return GPIO.input(button_pin)

def turnOnLED(pin_number):
    GPIO.output(pin_number, GPIO.HIGH) # Turn on

def turnOffLED(pin_number):
    GPIO.output(pin_number, GPIO.LOW)  # Turn off
    
def handleButtonDown():
    turnOnLED(8)
    sleep(1)                  # Sleep for 1 second
    turnOffLED(8)
    sleep(1)                  # Sleep for 1 second

setUpBoard()
while True: # Run forever
    if isButtonDown(10):
        handleButtonDown()