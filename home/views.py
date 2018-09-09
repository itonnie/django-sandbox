from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is home, home is where the heart is")