from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2Home(req):
    return HttpResponse('Home page Django chapter1 app2')