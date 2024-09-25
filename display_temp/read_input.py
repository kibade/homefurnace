#!/usr/bin/python
import RPi.GPIO as GPIO

def get_arm_position():

    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BCM) # Use BCM numbering e.g. BCM = 0 - on a model B GPIO 0 is on pin 11, confusing for sure.
    cat_arm = 17
    GPIO.setup(cat_arm, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    cat_arm_value = GPIO.input(cat_arm)
    return(cat_arm_value)
