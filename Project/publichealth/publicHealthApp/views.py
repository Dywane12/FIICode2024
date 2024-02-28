from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import User, Food
from django.template import loader


def index(request):
    return HttpResponse("<h1>Hello, world. You are at the start page.</h1>"
                        "<a href='/home/main' >Click to go to /home/main</a> <br>"
                        "<a href='/home' >Click to go to /home page</a> <br>"
                        "<a href='/login' >Click to go to /login</a> <br>"
                        "<a href='/register' >Click to go to /register</a> <br>"
                        "<a href='/' >Click to go back to start page</a>")

def index2(request):
    all_users = User.objects.all()
    all_foods = Food.objects.all()
    template = loader.get_template('publicHealthApp/index.html')
    context = {
        'all_users': all_users,
        'all_foods': all_foods
    }
    return HttpResponse(template.render(context, request))

def index3(request):
    return HttpResponse("<h1>Hello, this is /home/main page</h1>"
                        "<a href='/home' >Click to go back to /home </a> <br>"
                        "<a href='/' >Click to go back to start page</a>")

def login(request):
    template = loader.get_template('publicHealthApp/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def register(request):
    template = loader.get_template('publicHealthApp/register.html')
    context = {}
    return HttpResponse(template.render(context, request))