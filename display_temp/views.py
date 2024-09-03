from django.shortcuts import render
from django.http import HttpResponse
import random
from max31855 import MAX31855, MAX31855Error
import RPi.GPIO as GPIO
#from cat_arm import position

# Create your views here.
def get_temp (request):
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BCM) # Use BCM numbering e.g. BCM = 0 - on a model B GPIO 0 is on pin 11, confusing for sure.
    cs_pin = 24 #MAX is using BOARD = pin numbers not BCM
    clock_pin = 23
    data_pin = 22
    cat_arm = 0
    units = "c"
#    GPIO.setup(cat_arm, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    thermocouple = MAX31855(cs_pin, clock_pin, data_pin, units)
    thermocouple.cleanup()
    my_variable = random.randint(1, 100)
    GPIO.setup(cat_arm, GPIO.IN) # Input pin and set initial value to be pulled low (off)
    cat_arm_value = GPIO.input(cat_arm)
    GPIO.cleanup()
    return render(request, 'main.html', {'thermocouple': thermocouple,'cat_arm_value': cat_arm_value })

def say_hello(request):
    my_variable = random.randint(1, 1000)
    return render(request, 'main.html', {'my_variable': my_variable})

