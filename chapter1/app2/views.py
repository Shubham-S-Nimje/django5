from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2Home(req):
    return HttpResponse('Home page Django chapter1 app2')

def app2Status(req, **kwargs):
    status = kwargs.get('status')
    print(status)
    return HttpResponse(f'<h1>Hello Django status is: {status}</h1>')