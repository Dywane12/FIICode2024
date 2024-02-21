from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the publicHealthApp.</h1>"
                        "<a href='/home/main' >Click to go to main</a>")

def index2(request):
    return HttpResponse("<a href='/home' >Click to go home</a>")