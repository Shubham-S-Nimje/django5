from django.contrib import admin
from django.urls import path
from course.views import courseHome, courseAbout, courseUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', courseHome, name='home'),
    path('user', courseUser, name='user'),
    path('about', courseAbout, name='about')
]
