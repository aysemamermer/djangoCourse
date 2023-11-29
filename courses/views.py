from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(req):
    return HttpResponse('Home')


def courses(req):
    return HttpResponse('Courses')

