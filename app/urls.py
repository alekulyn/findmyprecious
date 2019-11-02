from django.urls import path
from . import views

urlpatterns = [
        path('',views.index, name='index'),
        path('signup', views.signup),
        path('signin', views.signin),
        path('addmarker', views.addmarker),
        path('getmarkers', views.getmarkers)
]
