## What is a 7 Segment Display?
A [7 segment display](https://en.wikipedia.org/wiki/Seven-segment_display) is an electronic device typically used to display numerical information.  Each digit consists of seven LED segments, and sometimes a decimal point or colon, which can be enabled programatically.

LEDs and how they are controlled

I2C commands??

![7Segment](/images/7SegmentDisplaySC.png)![7Segment](/images/7SegmentDisplaySC.png)![7Segment](/images/7SegmentDisplaySC.png)![7Segment](/images/7SegmentDisplaySC.png)

## 7 Segment Display Setup:
In order to use the 7 segment display from a Python program, we need to enable exteranl device communication on the Pi, and install a Python library to interact with the 7 Segment display.

### Enable External Device Communication

#### Configure RaspberryPi to allow communication with external devices

Connect to the Pi, and then run
```bash
sudo raspi-config
```

1) In the System Configurtion Menu choose Interface Options 
2) Enable both “SPI” and “I2C” interfaces
(Use your arrow keys to navigate and Enter to select).  
3) After enabling “SPI” and “I2C”, then exit the raspi-config utility and restart the pi.

    Restart by typing this command:
    ```bash
    sudo reboot now
    ```  
4) Wait for the Pi to restart (about 3 minutes) and then SSH back into the Pi.

### Install Python Library to work with 7 Segment Display (HT16k33 I2C Backpack) using PIP

1) Update linux package manager:
    ```bash
    sudo apt-get update
    ``` 

2) Download and install pip, the package manager for python libraries.
    ```bash
    sudo apt-get install python3-pip
    ``` 

3) Install HT16k33 I2C Backpack Python library
    ```
    pip3 install adafruit-circuitpython-ht16k33
    ```

### Wiring Diagram

![Seven Segment Wiring](/diagrams/7SevenSegmentDisplay_bb.png)

### Code Examples

#### Basic Setup
In order to use the I2C Backpack library, you will always need to perform the following setup.
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

#### Simple Display

#### Enabling decimal and clock

#### Characters


#### Challenges
