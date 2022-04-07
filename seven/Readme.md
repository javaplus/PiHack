# 7 Segment Displays
A [7 segment display](https://en.wikipedia.org/wiki/Seven-segment_display) is an electronic device typically used to display numerical information.  Each digit consists of seven LED segments, and sometimes a decimal point or colon, which can be enabled programatically.

Each segment, labeled A-G below, can be independently controlled. 

![7Segment](/images/7SegmentDisplaySC.png)![7Segment](/images/7SegmentDisplaySC.png)![7Segment](/images/7SegmentDisplaySC.png)![7Segment](/images/7SegmentDisplaySC.png)

## Wiring Diagram

![Seven Segment Wiring](/diagrams/7SevenSegmentDisplay_bb.png)

## Raspberry Pi Setup

In order to use the 7 segment display from a Python program, we need to enable external device communication on the Pi, and install a Python library to interact with the 7 Segment display.

### Enable External Device Communication


1) SSH to the Pi, and then run

    ```bash
    sudo raspi-config
    ```

2) In the **System Configuration** menu choose **Interface Options**
3) Enable both **“SPI”** and **“I2C”** interfaces
(Use your arrow keys to navigate and Enter to select).  
4) After enabling “SPI” and “I2C”, then exit the raspi-config utility and restart the pi.

    Restart by typing this command:
    ```bash
    sudo reboot now
    ```  
5) Wait for the Pi to restart (about 3 minutes) and then SSH back into the Pi.

### Install HT16k33 I2C Backpack library using PIP

1) Update the linux package manager (apt):
    ```bash
    sudo apt-get update
    ``` 

2) Download and install pip, the package manager for python libraries.
    ```bash
    sudo apt-get install python3-pip
    ``` 

3) Install the **HT16k33 I2C Backpack** Python library
    ```
    pip3 install adafruit-circuitpython-ht16k33
    ```
Now you are ready to program the 7 Segment Display!

## Python 

### Load and Initialize the Libraries 
In order to use the I2C Backpack library, you will need to perform the following setup in your Python program:
```python
import board
import busio
from adafruit_ht16k33 import segments

#### SETUP ######

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the LED segment class.
# This creates a 7 segment 4 character display:
display = segments.Seg7x4(i2c)
```
This makes a display object availble for you to interact with the display.

### Simple Display
To display data, we can either use the print function, or set each digit using an array.
```python
# Show 4218 on the display
display.print(4218)

# Set the first character to '1':
display[0] = '1'
# Set the second character to '2':
display[1] = '2'
# Set the third character to 'A':
display[2] = 'A'
# Set the forth character to 'B':
display[3] = 'B'
```

### Display time
To treat the display like a clock, we print a colon in addtion to the digits.
```python
# Set the display to 11:45
display.print(1145)
display.print(":")

# To turn off the colon, print a semicoln
disply.print(";")
```

### Display decimal
To display floating point numbers, we can simply print with a decimal point.
```python
# Display 1.389
display.print(1.389)
```

### Display text
Valid characters for the print function included letters 0-9, letters A-F, a period, and a hyphen.
```python
# Display 1-2.A
display.print("1-2.A")
```

### Display custom characters
To get more creative, you can use the set_digit_raw() method and enable segments to display your custom characters
```python
# Display 8.8.EE using Hex, and binary bitmask
display.set_digit_raw(0, 0xFF)
display.set_digit_raw(1, 0b11111111)
display.set_digit_raw(2, 0x79)
display.set_digit_raw(3, 0b01111001)
```


### Challenges
- Create a clock display where the colon blinks each second, and the time updates automatically
- Create a function to get the Pi's ip address and displays it as a marquee (hint: see the maruee() function)
- Create an animiation where a line revolves around the entire display

## Resources
https://docs.circuitpython.org/projects/ht16k33/en/latest/
https://learn.adafruit.com/matrix-7-segment-led-backpack-with-the-raspberry-pi