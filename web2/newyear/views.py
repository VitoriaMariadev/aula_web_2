from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(resquest):
    return render(resquest, "newyear/index.html", {
        'a': 'oii'
    })
