"""
URL configuration for chapter1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1.views import myfunction, home, app1Home
from app2.views import app2Home, app2Status

urlpatterns = [
    path('', home, name="Home"),
    path('admin/', admin.site.urls),
    path('chapter1/', myfunction, name="Chapter1 app1"),
    path('chapter1/app1', app1Home, name="Chapter1 app1"),
    path('chapter1/app2', app2Home, name="Chapter1 app2"),
    path('chapter1/app2/status', app2Status, {'status': 'OK'}, name="Chapter1 app2"),
    path('chapter1/app3', include('app3.urls'), name="Chapter1 app3"),
]
