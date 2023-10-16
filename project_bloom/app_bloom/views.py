from django.shortcuts import render
from django.http import HttpResponse
from app_bloom.urls import *

def home(request):
    return HttpResponse("funcionando"),
def hello(request):
    return HttpResponse("foi hello")
    
def gestao (request):
    return render(request, 'gestao.html')

def editargestao (request):
    return render(request, 'editargestao.html')

def doar (request):
    return render(request, 'doar.html')

def doarrecorrente (request):
    return render(request, 'doarrecorrente.html')

def doarunica (request):
    return render(request, 'doarunica.html')
