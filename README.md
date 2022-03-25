# PiHack

Run “sudo apt-get update” to update all the package repos for the apt-get utility.
Run “sudo apt-get install python3-pip” to install pip, the package manager for python libraries.
Run “sudo rasp-config” to enter the raspi-configuration setup.
Under Interface Options enable both “SPI” and “I2C”. (Use your arrow keys to navigate and Enter to select).  After enabling “SPI” and “I2C”, then exit the raspi-config utility and restart the pi.
Restart by typing this command: “sudo reboot”
Wait for about 3 minutes and then SSH back into the Pi.


## 7 Segment Display setup:


pip3 install adafruit-circuitpython-ht16k33

