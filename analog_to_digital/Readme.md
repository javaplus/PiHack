## Analog vs Digital

If you've followed the exercises and examples up to this point, you've seen how to tell if a button was pressed by watching the state of a GPIO pin change it's state from LOW to HIGH.  The GPIO pins on the Raspberry Pi only support digital signals by default.  That is they can only detect On or OFF (High or Low).  Really it's detecting if the voltage is high(~5 Volts) of if the voltage is low(~0 Volts)... these are digital signals.  But what if you wanted the Raspberry Pi to detect the amount of light in a room or the temperature.  These are things that cannot be reported by a simple digital response, that is just On or Off.  The temperature could be within a very wide range as could the measurement of light at a given time.  These two examples demonstrate analog signals.  Analog signals are continuous over time and their values could be theoretically infinite or at the least vary greatly. 

Actually most information in nature analog.  We've already mentioned two, but can you think of other things you can measure in nature that are both continuous and varying in their level?

## Analog to Digital Convertor 

There are many type of analog sensor avaliable... light and temperature sensors to vibration sesnsor and range sensor just to name a few.  But what if you want to use these on a Raspberry Pi that only accepts digital signals.  Well lucky for us there are Analog to Digital convertors.  These typically come in the form of a little chip called an integrated circuit (IC).  Integrated circuits or ICs are very common in electronics and can provide a wide range of functions.  The Analog to Digital convertor allows use any of these Analog sensors and send the data to the Raspberry Pi.  It does require a decent amount of wiring, but is not too difficult.  The ADC (analog digital convertor) connects to the SPI (serial periphal interface) of the pi.  The SPI is just a few dedicated GPIO pins that work together to allow us to talk to things like our ADC.  
The image below shows the SPI pins.  We will use all but one of these to connect our ADC.

![SPI Pins on Raspberry PI](/images/Pi-SPI-Pins.png)

## The Laser Tripwire!

For our project, we've been using a simple button to indicate the entering and exiting of the people in the line.  However, now we will replace the simple button as a sensor with a laser "tripwire".  The idea is that we will shine a laser beam (using a laser pointer) into a photoresistor (light sensor) to detect when someone has crossed the "beam" and entered or exited the line.  So, in our scenario, the photoresistor is the analog sensor that we will connect to our ADC.  The photoresistor works by resisting the flow of electricity when there's little to no light.  As you increase the amount of light shining on the photoresistor then the ressistence decreases and more electricity flows.  Therefore, when the photoresistor is properly connected to the Pi, it is constantly sending a signal of how much electricity is flowing through it.  If a super bright light is shining on it (like our laser pointer), then it will read max volts(in our case 5 volts).  If there is very little or no light it will read closer to 0 volts.  So, you can use this sensor to detect when someone gets in between the photoresistor and the laser beam therefore creating an electronic trip wire.


The diagram below demonstrates how to wire up the ADC and the photoresistor.  **NOTE:** The photoresitor does not connect directly to the Pi.  The photoresistor connects/talks to the ADC which translates its analog signal to the Pi.  Once you follow the diagram below to wire it up, you will need to run some code to test it out.  See the **ADC CODE** section below.



## Analog to Digital Convertor 

![Analog To Digital Convertor Diagram](/diagrams/PiZeroADC_PhotoResistor_bb.png)


## ADC CODE

Once you've got everything wired, you can simply copy the code found here: [ADC Code](/analog_to_digital/adc.py)

Create a file called "adc.py" on the Pi and then run this code to test the ADC and photoresitor.

If everything is working right, you should see a series of voltages being printed out.
As you cover the photoresistor to block out light, the voltages should decrease and if you shine a light or laser at the photoresistor you should see the voltages increase.

## Using the ADC Code in your Program

The "adc.py" program that you used to test your wiring can also be imported and used by your program to easily get the value from the photoresistor.
Creating shareable code is very common in software development.  In Python, if you import another python program into your file, you can access it's functions.  
So, in our case if we import the adc.py file into our program, you can simply call the **adc.get_adc(0)** to get the value of the sensor connected to the ADC.  The zero is to say get the value for the first device.  If you connect two photoresistors, the second would connect to the only unused pin left on the ADC chip.  Then you could get it's value by calling **adc.get_adc(1)**.

See the [tripwire.py](/analog_to_digital/tripwire.py) file as an example.  This program will light up the LED if the tripwire is tripped for more than two seconds.
