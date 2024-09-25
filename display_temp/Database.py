from .models import Temperture_Data

def save_temp(temp, cat_arm_value):
    # Save new recording to the database Temperture_Data
    recorded_temp = Temperture_Data()
    recorded_temp.temperture = temp
    recorded_temp.arm = cat_arm_value
    recorded_temp.save()
    return()
