#!/usr/bin/python
from display_temp.max31855 import MAX31855, MAX31855Error

def read_temp (): 
#####################################
#Gets values to display on main page
#####################################
    cs_pin = 24 #MAX is using BOARD = pin numbers not BCM
    clock_pin = 23
    data_pin = 22
    units = "c"
    thermocouple = MAX31855(cs_pin, clock_pin, data_pin, units)
    temp = thermocouple.get() 
    temp = 900
    thermocouple.cleanup()
    return(temp)
