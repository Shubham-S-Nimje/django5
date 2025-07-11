from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return HttpResponse('Home page Django')

def app1Home(req):
    return HttpResponse('Home page Django chapter1 app1')

def myfunction(req):
    return HttpResponse('<h1>Hello Django chapter1 app1</h1>') 