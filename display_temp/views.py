# Displays Main page for furnace temp
from django.shortcuts import render
from django.http import HttpResponse
import random
from max31855 import MAX31855, MAX31855Error
from read_input import get_arm_position
from read_temp import read_temp
from .models import Temperture_Data

# Create your views here.
def get_temp (request): 
    temp = read_temp() #reads thremocouple temp from Max31855
    # Save new recording to the database Temperture_Data
    recorded_temp = Temperture_Data()
    recorded_temp.temperture = temp
    ################
    cat_arm_value = get_arm_position()  #reading arm position
    recorded_temp.arm = cat_arm_value
    recorded_temp.save()
    return render(request, 'main.html', {'temp': temp,'cat_arm_value': cat_arm_value })
