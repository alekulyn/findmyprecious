from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader

from django.contrib.auth.models import User
from .models import Item
from .forms import *

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {"G_MAP_API": "IzaSyCUQV1j3kOLztOTQSnBJQmzEND3N1-_y5Q"}
    return HttpResponse(template.render(context, request))

def signup(request):
    #username = request.GET['user']
    #password = request.GET['pass']
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/sign-up/')
    else:
        form = SignUp()
    new_user = User.objects.create_user(username=username, password=password)
    new_user.save()

    return render(request, 'index.html', {'form': form})

def signin(request):
    username = request.GET['user']
    password = request.GET['pass']

    user = authenticate(username=username, password=password)

    if user is not None:
        return HttpResponse("Success")
    else:
        return HttpResponse("Failure")

def addmarker(request):
    user = User.object() #Get current user
    Item.objects.create(user=user, latitude=request.POST['latitude'], longitude=request.POST['longitude'], title=request.POST['title'])
    pass

def getmarkers(request):
    context = None
    pass
