# Tem que criar na aplicação esse arquivo urls.py 

from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>/", views.contatos, name="contatos"), # Como passar um parametro pela URL
]
