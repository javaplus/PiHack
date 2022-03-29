# Originally by Mikey Sklar for Adafruit Industries
# Modified slightly to make simple examples

import time
import board
import busio
from adafruit_ht16k33 import segments

#### SETUP ######

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)

# Clear the display.
display.fill(0)

##### END SETUP ####

### Below here are various ways to write out to the display ###

# Can just print a number
display.print(42)
time.sleep(1)

# Set the first character to '1':
display[0] = '1'
# Set the second character to '2':
display[1] = '2'
# Set the third character to 'A':
display[2] = 'A'
# Set the forth character to 'B':
display[3] = 'B'
time.sleep(1)

numbers = [0.0, 1.0, -1.0, 0.55, -0.55, 10.23, -10.2]

# print negative and positive floating point numbers
for i in numbers:
    display.print(i)
    time.sleep(0.5)

time.sleep(1)
# print just a value and add the colon:
display.print(1145)
display.print(":")
