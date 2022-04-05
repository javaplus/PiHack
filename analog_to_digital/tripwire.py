import adc
import time
import RPi.GPIO as GPIO

# Variable to hold how long the tripwire has been tripped
tripped_time_sec = 0
# Variable to keep track if something "tripped" the beam
is_tripped = False
# Variable for storing what "tripped" threshold should be in volts
TRIPPED_THRESHOLD=2.3
# Pin number for our LED
LED_PIN=8
#Variable for total time in seconds to be tripped to count as entered/exited
TRIPPED_TIME_FOR_COUNT=2

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)

def light_on():
  print("light up!!!!!!!!!!!!!!!!!!!")  
  GPIO.output(LED_PIN, GPIO.HIGH) # Turn on


def light_off():
  print("light off??????")  
  GPIO.output(LED_PIN, GPIO.LOW) # Turn on

def check_entrance_switch():
  global is_tripped
  global tripped_time_sec
  voltage = adc.get_adc(0)
  print("ADC Channel 0:", round(voltage, 2), "V")
  if(voltage < TRIPPED_THRESHOLD):
     # see if tripped for more than 2 seconds
     if(is_tripped):
       tripped_time_sec = tripped_time_sec + time.time()
       if(tripped_time_sec > TRIPPED_TIME_FOR_COUNT):
         light_on()
     else:
       tripped_time_sec = 0
       is_tripped = True
    # else not tripped (not dropped below 2.3v
  else:
     tripped_time_sec = 0
     is_tripped = False
     light_off()

# Report the photoresistor  voltages to the terminal
try:
  while True:
   check_entrance_switch()
   time.sleep(0.2)

except KeyboardInterrupt:
  GPIO.cleanup()

