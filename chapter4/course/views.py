from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(req):
    html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Chapter4 Home</title></head><body><h1>Chapter4 Home</h1></body></html>'
    return HttpResponse(html)

def courseHome(req):
    d = datetime.now()
    actors = {'ironman', 'thor', 'hulk', 'spider'}
    course_details = {'chapterName': 'chapter4 course home'}
    return render(req, 'course/index.html', context={'course_details': course_details, 'datetime': d, 'names':actors})
