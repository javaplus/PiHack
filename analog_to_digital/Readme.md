## I Need More Data from Sensor

If you've followed the exercises and examples up to this point, you've seen how to tell if a button was pressed by watching the state of a GPIO pin change it's state from LOW to HIGH.  The GPIO pins on the Raspberry Pi only support digital signals be default.  That is they can only detect On or OFF (High or Low).  Really it's detecting if the voltage is high(~5 Volts) of if the voltage is low(~0 Volts).  But what if you wanted the Raspberry Pi to detect the amount of light in a room or the temperature.  These are things that cannot be reported by a simple digital responss that is just On or Off.  The temperature could be within a vary wide range as could the measurement of light at a given time.  These two examples demonstrate analog signals.  Analog signals are continuous over time and their values could be theoretically infinite. 

Actually most signals in nature analog.  We've already mentioned two, but can you think of other things you can measure in nature that are both continuous and varying in their level?

Many 


## Analog to Digital Convertor 

![Analog To Digital Convertor Diagram](/diagrams/PiZeroADC_PhotoResistor_bb.png)
