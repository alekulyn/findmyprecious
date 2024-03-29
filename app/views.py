from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json

from django.contrib.auth.models import User
from .models import Item

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {"G_MAP_API": "IzaSyCUQV1j3kOLztOTQSnBJQmzEND3N1-_y5Q"}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def signup(request):
    username = request.POST['user']
    password = request.POST['pass']
    email = request.POST['email']

    new_user = User.objects.create_user(username=username, password=password, email=email)
    new_user.save()
    return HttpResponse("success")

@csrf_exempt
def signin(request):
    username = request.POST['user']
    password = request.POST['pass']

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponse(json.dumps({'status':"success",'name':username}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'status':"failure"}), content_type="application/json")

@csrf_exempt
def logout_user(request):
    logout(request)
    return HttpResponse("success")

@csrf_exempt
def addmarker(request):
    item = Item.objects.create(user=request.user, latitude=request.POST['latitude'], longitude=request.POST['longitude'], title=request.POST['title'], desc=request.POST['desc'], found=(request.POST['found'] == 'true'))
    item.save()
    return HttpResponse("success")

@csrf_exempt
def getmarkers(request):
    pins = [{'user':p.user.username, 'email':p.user.email, 'latitude':p.latitude, 'longitude':p.longitude, 'title':p.title, 'desc':p.desc, 'found':p.found} for p in Item.objects.all()]
    return HttpResponse(json.dumps({'status':"success",'pins':json.dumps(pins)}), content_type="application/json")
