## 7 Segment Display setup:

#### Update linux package manager:
Run:```sudo apt-get update``` 
#### Download and install pip, the package manager for python libraries.
Run:```sudo apt-get install python3-pip```
#### Configure RaspberryPi to allow communication with external devices
Run:```sudo rasp-config```

Under Interface Options enable both “SPI” and “I2C”. 
(Use your arrow keys to navigate and Enter to select).  
After enabling “SPI” and “I2C”, then exit the raspi-config utility and restart the pi.
Restart by typing this command:   
Run:```sudo reboot```  
Wait for about 3 minutes and then SSH back into the Pi.

### Install Python Library to work with 7 Segment Display (HT16k33 I2C Backpack)

Run: ```pip3 install adafruit-circuitpython-ht16k33```

### Wiring Diagram

![Seven Segment Wiring](/diagrams/7SevenSegmentDisplay_bb.png)
