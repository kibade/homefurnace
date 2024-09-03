from django.shortcuts import render
from django.http import HttpResponse
import random
from max31855 import MAX31855, MAX31855Error
from read_input import get_arm_position
# Create your views here.
def get_temp (request):
    cs_pin = 24 #MAX is using BOARD = pin numbers not BCM
    clock_pin = 23
    data_pin = 22
    units = "c"
    thermocouple = MAX31855(cs_pin, clock_pin, data_pin, units)
    thermocouple.cleanup()
    cat_arm_value = get_arm_position()
    return render(request, 'main.html', {'thermocouple': thermocouple,'cat_arm_value': cat_arm_value })

def say_hello(request):
    my_variable = random.randint(1, 1000)
    return render(request, 'main.html', {'my_variable': my_variable})

