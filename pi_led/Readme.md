## Programming the RaspberryPi

This will be our first exercise actually writing code for the Rapsberry Pi.  We will connect our LED to one of the Raspberry Pi's GPIO (General Purpose Input Output) pins to light the LED when our code tells it to.

The code for this exercise is provided for you.  It's a simple Python program that just initializes the GPIO pins appropriately and then continually loops and lights the LED for 1 second and then turns it off for 1 second.

## The Code!
It's recommended to type this code so you become more familar with each line:
```
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)

while True: # Run forever
    GPIO.output(8, GPIO.HIGH) # Turn on
    sleep(1)                  # Sleep for 1 second
    GPIO.output(8, GPIO.LOW)  # Turn off
    sleep(1)                  # Sleep for 1 second
```

## Wiring Diagram
![Pi with LED](/diagrams/5LEDControlWithPi_bb.png)
