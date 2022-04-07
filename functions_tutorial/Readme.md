# Intro to Functions
Functions are necessary when building out any program larger than a simple Hello World demo.  They help break up code into tasks that can be re-used and make testing and debugging your code a lot easier.  Functions allow your program to be broken out into manageable pieces.  Functions can take in parameters to be used.  As we go through some principles, we will see parameters being used.  Using the button.py function we just created, we'll go through a couple of important principles to follow when making functions.

# DRY Principle
The DRY princple stands for Don't Repeat Yourself.  When writing code, we do not want to repeatedly use the same line of code throughout our program.  An example of code **not** using the DRY principle would be using a single formula numerous times.
### Bad example not using the DRY principle
```
temp = 55
new_temp = ((temp - 32) * (5 / 9)) + 273.15

temp2 = 46 
new_temp_k = ((temp2 - 32) * (5 / 9)) + 273.15
```
As you can see, the same formula is used more than once.  Repeating yourself numerous times while coding can lead to human error and make it more difficult to update code when necessary,  Instead, create a function that contains the line of code.  This allows for a smaller chance of human error and allows you to update every spot where the code is used only once.
```
def calculateTemp(temp):
  new_temp = ((temp - 32) * (5 / 9)) + 273.15
  return new_temp
  
temp = 55
new_temp = calculateTemp(temp)

temp2 = 46
new_temp_k = calculateTemp(temp2)
```

# SOLID Principle (Single Responsibility)
The SOLID Principles are 5 software design principles for creating better code.  Today we will only be focusing on the **S** in SOLID.  The **S** stands for the Single Responsibility Principle (SRP).  The SRP states that every class, method, or function should only have one responsibility or task.  When looking at our current button.py program, there's nothing inherintely wrong with it.  However, we could make it better and more concise.  Our current program has no functions.
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
Using SRP, we can break each step of this program down into their own functions.  If we look at line 4-8, this is where we set up the board.
```
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # Set pin 10 to be an input pin and set initial value to low (off)
```
Instead, we should break these out into their own function called setUpBoard().  This function follows the SRP by having one job, which is to set the board up in our python program.
```
def setUpBoard():
    GPIO.setwarnings(False)    # Ignore warning for now
    GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # Set pin 10 to be an input pin and set initial value to low (off)
```
Inside the while loop on line 10, we have an if statement checking if the button has been pushed.
```
if GPIO.input(10) == GPIO.HIGH:
```
This line can be broken out into a function titled isButtonDown().  The function will take a parameter that obtains the pin number.  We can then use this function to replace the equation on line 11.
```
def isButtonDown(button_pin):
    return GPIO.input(button_pin)
    
while True: # Run forever
  if isButtonDown(10):
```
Inside the if statement, we can separate some of this in to it's own functionality as well.
```
GPIO.output(8, GPIO.HIGH) # Turn on
sleep(1)                  # Sleep for 1 second
GPIO.output(8, GPIO.LOW)  # Turn off
sleep(1)                  # Sleep for 1 second
```
On line 12, we turn the LED on.  This can be broken out into it's own function titled turnOnLED().  On line 14, we turn the LED off.  This can alo be broke out into it's own function titled turnOffLED().  Both of these functions will take in the pin number as a parameter.
```
def turnOnLED(pin_number):
    GPIO.output(pin_number, GPIO.HIGH) # Turn on

def turnOffLED(pin_number):
    GPIO.output(pin_number, GPIO.LOW)  # Turn off
```
Finally, we can wrap the entire functionaliy of the if statement in another function titled handleButtonDown().  This will use the sleep() functions and our two turnOnLED() and turnOffLED() functions to run the desired output.
```
def handleButtonDown():
    turnOnLED(8)
    sleep(1)                  # Sleep for 1 second
    turnOffLED(8)
    sleep(1)                  # Sleep for 1 second
```
Now that we have separated out the code into functions, we can call them like this.
```
setUpBoard()
while True: # Run forever
    if isButtonDown(10):
        handleButtonDown()
```
When put all together, we can see how this button.py, while larger than the original, is more concise and will lead to better programming.
```
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
```
