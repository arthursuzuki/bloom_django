from django.urls import path,include
from django.http import HttpResponse
from app_bloom.views import *
from app_bloom.views import editargestao, doar, doarrecorrente, doarunica


urlpatterns = [
    path('',home),
    path('hello/',hello,name="name"),
    path('doar/',doar),
    path('doar/recorrente/',doarrecorrente),
    path('doar/unica/', doarunica),
]
