from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Chapter5 Home</title></head><body><h1>Chapter5 Home</h1></body></html>'
    return HttpResponse(html)

def courseHome(req):
    return render(req, 'course/index.html')
