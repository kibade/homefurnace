from django.shortcuts import render
from django.http import HttpResponse
import random
from max31855 import MAX31855, MAX31855Error
# Create your views here.
def get_temp (request):
    cs_pin = 24
    clock_pin = 23
    data_pin = 22
    units = "c"
    thermocouple = MAX31855(cs_pin, clock_pin, data_pin, units)
    thermocouple.cleanup()
    my_variable = random.randint(1, 1000)
    return render(request, 'main.html', {'thermocouple': thermocouple})

def say_hello(request):
    my_variable = random.randint(1, 1000)
    return render(request, 'main.html', {'my_variable': my_variable})

