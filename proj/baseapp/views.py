from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {"id": 1, "name": "Lets Learn Python!"},
    {"id": 2, "name": "Lets Learn Javascript!"},
    {"id": 3, "name": "Lets Learn C#!"},
]


def home(request):
    return render(request, "baseapp/home.html", {"rooms": rooms})

def room(request, pk):
    return render(request, "baseapp/room.html")