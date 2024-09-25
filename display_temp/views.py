# Displays Main page for furnace temp
from django.shortcuts import render
from django.http import HttpResponse
import random
from display_temp.max31855 import MAX31855, MAX31855Error
from display_temp.read_input import get_arm_position
from display_temp.read_temp import read_temp


# Create your views here.
def get_temp (request): 
    temp = read_temp() #reads thremocouple temp from Max31855
    cat_arm_value = get_arm_position()  #reading arm position
    return render(request, 'main.html', {'temp': temp,'cat_arm_value': cat_arm_value }) #Displays on webpage
