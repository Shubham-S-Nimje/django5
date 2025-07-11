from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return render(req, 'core/home.html')
def menu(req):
    return render(req, 'core/menu.html')
def ordertrack(req):
    return render(req, 'core/ordertrack.html')
def reservation(req):
    return render(req, 'core/reservation.html')
def contact(req):
    return render(req, 'core/contact.html')