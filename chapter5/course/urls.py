from django.contrib import admin
from django.urls import path
from course.views import courseHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', courseHome, name='home')
]
