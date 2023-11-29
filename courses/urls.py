from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('courses', views.courses),
]
