# PiHack

Repository for learning electronics basics and how to code on the Raspberry Pi!


Below are the links for the hands on exercises to learn how to work with simple electronics and programming with the Raspberry Pi.
The Basic Exercises are designed to give you the foundation to which to build off of.  The Basic Exercises give you all the instructions to complete them.
Once you complete the Basics, you should have some basic understanding of how to work with the Raspberry Pi to record inputs and control LEDs.
From there, the Extensions can help you add to your project to make it more challenging and exciting!

## What are we trying to do here?

- Read the overview of our problem statement here! [Project Overview](/project_overview/overview.md)

## Prerequisites

Install Thonny by following these [instructions](/thonny).


## Basic Exercises:

- [First Circuit](./first_circuit)
- [Resistors](./resistor)
- [Simple Button](./simple_button)
- [Intro To Raspberry Pi](./pi_power)
- [Programming the Pi](./pi_led)
- [Input with the Pi](./pi_button)
- [Using Functions](./functions_tutorial)

## What Now?

After completing the Basic Exercises, you should have the basic understanding of how to read input using the GPIO pins and work with simple LEDs.
Now take what you've learned and review the [Project Overview](/project_overview/overview.md) once again and think about how you can start gathering the required information.  Perhaps an easy way to start is to use a button as a place holder for a turnstile/gate that tracks when students enter the line.  A second button could be used as an exit gate.  Then through the code you could have logic to keep count of numbers in line over time.  Start brainstorming and start coding!

For more ways to extend your project, look at the **Extensions** section below for how to add things like a display for numbers or even an optical turnstie/tripwire.

Code on!

## Extensions
- [7 Segment Display](./seven)
- [Analog to Digital](./analog_to_digital)


## Additional Resources
#### New to Python:
- [Getting Started with Pyton (hands-on)](https://www.programiz.com/python-programming/first-program)
- [Python Functions](https://www.freecodecamp.org/news/functions-in-python-a-beginners-guide/)
- [Working with Time](https://www.programiz.com/python-programming/time)
- [While Loops in Python](https://www.w3schools.com/python/python_while_loops.asp)
- [Global Variables in Python](https://www.w3schools.com/python/python_variables_global.asp)
- [Python If Else Statement](https://www.programiz.com/python-programming/if-elif-else)

#### Advanced RaspberryPi With Python:
- [RaspberryPi Interrupt](./interrupt)


## Parts List:
### 7 Segment Displays
NOTE:  When getting 7 Segment displays to work with the Pi, get the ones with the I2C backpack included. Otherwise, it requires a lot more wires and more coding.
- [.56" Displays - Amazon](https://www.amazon.com/Adafruit-4-Digit-7-Segment-Display-Backpack/dp/B00GJRW0DS?th=1)
- [.56" Displays - Adafruit](https://www.adafruit.com/product/881)
- [.56" Displays - Microcenter](https://www.microcenter.com/product/504149/adafruit-industries-056-4-digit-7-segment-display-w-i2c-backpack-blue)
- [.56" Displays - Chicago Elec Dist](https://chicagodist.com/collections/adafruit/products/adafruit-0-56-4-digit-7-segment-display-w-i2c-backpack-red)
- [1.2" Displays - Adafruit](https://www.adafruit.com/product/1269)
- [1.2" Displays - Chicago Elec Dist](https://chicagodist.com/collections/adafruit/products/adafruit-1-2-4-digit-7-segment-display-w-i2c-backpack-red)
### Analog to Digital Convertor (MCP3002):
NOTE: The MCP3002 ADC was used in this tutorial mainly used because they are cheaper to get and have decent library support.  If not following this tutorial, I'd recommend looking at the alternative MCP3008.
- [MCP3002 ADC - Sparkfun](https://www.sparkfun.com/products/8636)
- [MCP3002 ADC - Amazon](https://smile.amazon.com/MCP3002-I-Analog-Digital-Converter-Single/dp/B005T6BJUA/ref=sr_1_2?crid=I60G379BCH4Y&keywords=mcp3002&qid=1649782181&sprefix=mcp3002%2Caps%2C97&sr=8-2)
- [MCP3002 ADC - Mouser](https://www.mouser.com/ProductDetail/Microchip-Technology/MCP3002-I-P?qs=Ux5rHyN1IXSXX8XkfIMKEg%3D%3D)
- [MCP3002 ADC - Digi-Key](https://www.digikey.com/en/products/detail/microchip-technology/MCP3002-I-P/319412)
### Alternative Analog to Digital Convertor(MCP3008)
NOTE: The MCP3008 is slightly more expensive than the MCP3002, but supports more input and has better library support and documentation.
- [MCP3008 ADC - Mouser](https://www.mouser.com/ProductDetail/Microchip-Technology/MCP3008-I-P?qs=AF%252BffTaPb30XZ0OdV6HdVg%3D%3D)
- [MCP3008 ADC - Digi-Key](https://www.digikey.com/en/products/detail/microchip-technology/mcp3008-i-p/319422)
- [MCP3008 ADC - Chicago Elec Dist](https://chicagodist.com/products/8-channel-10-bit-analog-adc-for-raspberry-pi)
- [MCP3002 ADC-Adafruit](https://www.adafruit.com/product/856)
### General Kits
Note: Kits to include wires, breadboard, resistors, photoresistors(light sensors), etc...
- [Basic Electronics Kits](https://www.amazon.com/REXQualis-Electronics-tie-Points-Breadboard-Potentiometer/dp/B073ZC68QG/ref=sr_1_5?keywords=electronics+starter+kit&qid=1644431922&sprefix=electronics+startr%2Caps%2C132&sr=8-5)
