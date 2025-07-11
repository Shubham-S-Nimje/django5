from django.urls import path
from course.views import courseHome

urlpatterns = [
    path('', courseHome, name='home')
]
