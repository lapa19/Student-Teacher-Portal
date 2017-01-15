from django.http import HttpResponse 
from django.template.loader import get_template
from django.template import Context
import datetime 
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})
