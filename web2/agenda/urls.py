# Tem que criar na aplicação esse arquivo urls.py 

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:id>/", views.contatos, name="contatos"), # Como passar um parametro pela URL
]
