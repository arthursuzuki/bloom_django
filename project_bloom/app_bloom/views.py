from django.shortcuts import render
from django.http import HttpResponse
from app_bloom.urls import *

def home(request):
    return HttpResponse("funcionando"),
