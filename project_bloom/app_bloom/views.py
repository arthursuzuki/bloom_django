from django.shortcuts import render
from django.http import HttpResponse
from app_bloom.urls import *

def home_page(request):
    return render(request,'inicial/header.html')
def menu(request):
    return render(request,'inicial/menu.html')
def login(request):
    return render(request,'inicial/login.html')
def doar (request):
    return render(request, 'inicial/doar.html')

def doarrecorrente (request):
    return render(request, 'inicial/doarrecorrente.html')

def doarunica (request):
    return render(request, 'inicial/doarunica.html')
