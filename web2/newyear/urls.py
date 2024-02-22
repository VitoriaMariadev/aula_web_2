# Tem que criar na aplicação esse arquivo urls.py 

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
