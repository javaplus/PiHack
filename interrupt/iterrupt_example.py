#!/usr/bin/env python3          
                                
import signal                   
import sys
import RPi.GPIO as GPIO

ENTER_BUTTON_GPIO = 15
EXIT_BUTTON_GPIO = 18
LED_GPIO = 14

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
    
def line_enter_callback(channel):
    if(GPIO.input(ENTER_BUTTON_GPIO)):
      GPIO.output(LED_GPIO, GPIO.HIGH)
    else:
      GPIO.output(LED_GPIO, GPIO.LOW)
      
def line_exit_callback(channel):
    if(GPIO.input(EXIT_BUTTON_GPIO)):
      GPIO.output(LED_GPIO, GPIO.HIGH))
    else:
      GPIO.output(LED_GPIO, GPIO.LOW)
      
      
#  This protects whatever code is placed beneath it from being executed when imported.  It is essentially defining this file as an application not a module.
if __name__ == '__main__':
#   This will disable runtime warning from crashing the app. Starting and stopping the app can create runtime warning depending on how it is stopped. 
#   do this for a better developer experience.
    GPIO.setwarnings(False)  

    GPIO.setup(ENTER_BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(EXIT_BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(LED_GPIO, GPIO.OUT)   
    GPIO.add_event_detect(ENTER_BUTTON_GPIO, GPIO.BOTH, callback=line_enter_callback)
    GPIO.add_event_detect(EXIT_BUTTON_GPIO, GPIO.BOTH, callback=line_exit_callback)
    
#   The signal.SIGINT sends a keyboard event when 'control c' is pressed and signal_handler cleans up the GPIO assignments and closes the app.
    signal.signal(signal.SIGINT, signal_handler)
#   These will pause the execution flow of the app so that the script stays open in the console and the callbacks stay active.
    signal.pause()
    

