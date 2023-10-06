from django.urls import path,include
from django.http import HttpResponse
from app_bloom.views import *


urlpatterns = [
    path('',home(),name=''),
]
