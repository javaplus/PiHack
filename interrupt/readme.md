# RaspberryPi Interrupt
A GPIO interrupt allows for callback methods to be executed asynchronously on a signal event, corresponding to input like a button.  When the button is pressed the callback function gets executed. The following method `add_event_detect` is used to setup the interrput and it takes 3 parameters, the first is the GPIO pin number, the second is the trigger condition, the third is the callback function.
```python
GPIO.add_event_detect(ENTER_BUTTON_GPIO, GPIO.BOTH, callback=line_enter_callback)
```
The second parameter can be `GPIO.RISING`, `GPIO.FALLING` or `GPIO.Both`.  It will trigger the callback function when the gpio pin goes from a state of low energy to high energy (**RISING CHANGE**), a state of high energy to low energy (**FALLING CHANGE**), or be triggered twice... once on the way up then again on the way back down.   

![Arduino interrput Model](/diagrams/arduino_interrupt_mode.jpg)


The above iterrupt_example.py is based off of the following article...
- [RaspberryPi Interrupt](https://roboticsbackend.com/raspberry-pi-gpio-interrupts-tutorial/)


