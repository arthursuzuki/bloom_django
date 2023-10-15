from django.shortcuts import render
from django.http import HttpResponse
from app_bloom.urls import *

def hello(request):
    return render(request,'inicial/inicial.html')
