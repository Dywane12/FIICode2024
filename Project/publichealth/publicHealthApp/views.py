from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. You are at the start page.</h1>"
                        "<a href='/home/main' >Click to go to /home/main</a> <br>"
                        "<a href='/home' >Click to go to /home page</a> <br>"
                        "<a href='/' >Click to go back to start page</a>")

def index2(request):
    return HttpResponse("<h1>Hello, this is /home page</h1>"
                        "<a href='/home/main' >Click to go to /home/main </a> <br>"
                        "<a href='/' >Click to go back to start page</a>")

def index3(request):
    return HttpResponse("<h1>Hello, this is /home/main page</h1>"
                        "<a href='/home' >Click to go back to /home </a> <br>"
                        "<a href='/' >Click to go back to start page</a>")