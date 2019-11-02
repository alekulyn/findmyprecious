from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from .models import Item

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def signup(request):
    username = request.POST['user']
    password = request.POST['pass']
    
    new_user = User.objects.create_user(username=username, password=password)
    new_user.save()
    return HttpResponse("success")

def signin(request):
    username = request.POST['user']
    password = request.POST['pass']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponse("success")
    else:
        return HttpResponse("failure")

def addmarker(request):
    user = User.object() #Get current user
    Item.objects.create(user=user, latitude=request.POST['latitude'], longitude=request.POST['longitude'], title=request.POST['title'])
    pass

def getmarkers(request):
    context = None
    pass
