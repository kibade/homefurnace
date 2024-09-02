from django.shortcuts import render
from django.http import HttpResponse
import random
from max31855 import MAX31855, MAX31855Error
# Create your views here.
def say_hello(request):
    my_variable = random.randint(1, 100)
    return render(request, 'main.html', {'my_variable': my_variable})

