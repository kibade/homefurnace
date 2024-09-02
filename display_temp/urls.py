from django.urls import path
from . import views


#URL CONF
urlpatterns = [
    path('hello/', views.say_hello)
]

