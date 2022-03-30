## Vive la Resistance!

The LED we used in our first circuit is like most electronics in that it was created to work within a certain voltage range. 
See the highlighted part of the description below that states the rating for this a simple red LED like we are using:
![Red LED Description](/images/LEDDescription.PNG)

As you can see, the typical rating of a red LED like this is 2volts.  Our current power source is outputting about 5volts... too much for this LED! 
If your power source is too high (like in our case) there's the potential of "frying"(damaging) the equipment.  
To allow a higher voltage power source to work with your LED, we need something that can "resist" the flow of electricity to bring it to a safe level to work with our LED.
That is what a **resistor** does.  A **Resistor** resists the flow of electricity.  So, adding a resistor into our circuit can help control the amount of power flowing through the LED.

Here is a neat online calculator to calculate the type of resistor you need:
[LED resistor calculator](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-led-series-resistor)

Now we will make one minor change to our circuit to keep our LED from frying.  We will simply connect the LED to the ground/negative side with a resistor so that it operates in safe ranges.


## Wiring Diagram

![LED With Resistor](/diagrams/2LEDWResistor_bb.png)


## Optional Experiment

You could experiment with different resistors to see how it affects the brightness of the LED.  Perhaps try a 1K and a 10K resistor and see how each affect the LED.
