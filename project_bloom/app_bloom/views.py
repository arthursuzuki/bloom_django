from django.shortcuts import render
from django.http import HttpResponse
from app_bloom.urls import *

def home_page(request):
    return render(request,'inicial/header.html')
