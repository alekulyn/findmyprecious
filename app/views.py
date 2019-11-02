from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
import json

from django.contrib.auth.models import User
from .models import Item

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {"G_MAP_API": "IzaSyCUQV1j3kOLztOTQSnBJQmzEND3N1-_y5Q"}
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
        return HttpResponse(json.dumps({'status':"success",'name':username}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'status':"failure"}), content_type="application/json")

def addmarker(request):
    Item.objects.create(user=request.user, latitude=request.POST['latitude'], longitude=request.POST['longitude'], title=request.POST['title'], desc=request.POST['desc'])
    return HttpResponse()

def getmarkers(request):
    pins = [(p.User.username, p.latitude, p.longitude, p.title, p.desc, p.found) for p in Item.objects.all()]
    return HttpResponse(json.dumps({'status':"success",'pins':json.dumps(pins)}), content_type="application/json")
