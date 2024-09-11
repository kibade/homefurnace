from django.urls import path
from . import views


#URL CONF
urlpatterns = [
    path('', views.get_temp)
]

