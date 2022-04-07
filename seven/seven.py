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
# Show 4218 on the display
display.print(4218)

time.sleep(2)

# Set the first character to '1':
display[0] = '1'
# Set the second character to '2':
display[1] = '2'
# Set the third character to 'A':
display[2] = 'A'
# Set the forth character to 'B':
display[3] = 'B'

time.sleep(2)

# Set the display to 11:45
display.print(1145)
display.print(":")

time.sleep(2)

# Display 1.389
# Disable the colon
display.print(";")
display.print(1.389)

time.sleep(2)

# Display 1-2.A
display.print("1-2.A")

time.sleep(2)

# Display 8.8.EE using Hex, and binary bitmask
display.set_digit_raw(0, 0xFF)
display.set_digit_raw(1, 0b11111111)
display.set_digit_raw(2, 0x79)
display.set_digit_raw(3, 0b01111001)