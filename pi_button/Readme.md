## Input to the Raspberry Pi

We've seen how to use a Raspberry Pi to control an LED.  This was done by setting the GPIO pin to Ouput mode.  This would allow the GPIO pin to send power to the LED when we set the pin to "High".
But how do we recieve input to the Pi.  That is to use sensors or tell when a button is pressed.  
Well that's what this exercise is for.   
In this exercise, we will show how to use a GPIO pin to receive input.  In our case, the input will be to detect when a button is pressed.

## The Code:
Here is the code.  Notice this time you simply add two new lines to the previous code.  That is you will add the GPIO setup for the pin 10 to be Output.
Then you will had an if condition to only light the LED if the button is pressed.

```
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # Set pin 10 to be an input pin and set initial value to low (off)

while True: # Run forever
  if GPIO.input(10) == GPIO.HIGH:
    GPIO.output(8, GPIO.HIGH) # Turn on
    sleep(1)                  # Sleep for 1 second
    GPIO.output(8, GPIO.LOW)  # Turn off
    sleep(1)                  # Sleep for 1 second
```

## Wiring Diagram

For the code above to work, you need to connect one side of the button to the pin 10 on the Pi.  This is acting as a Ground to detect when electricity is flowing and thus is "High".

![Pi with Button and LED Diagram](/diagrams/6LEDAndButtonWithPi_bb.png)
