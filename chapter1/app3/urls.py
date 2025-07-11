from django.urls import path
from app3.views import app3Home

urlpatterns = [
    path('', app3Home, name="Chapter1 app3"),
]
