from django.urls import path,include
from django.http import HttpResponse
from app_bloom.views import *
from app_bloom.views import editargestao, doar, doarrecorrente, doarunica

urlpatterns = [
    path('',menu,name="home"),
    path('hello/',home_page,name="name"),
    path('sobre/',home_page,name="sobre"),
    path('login/padrinho/',home_page,name="l_padrinho"),
    path('contribuir/',home_page,name="contribuir"),
    path('logins/',login,name="opc_login"),
    path('doar/',doar),
    path('doar/recorrente/',doarrecorrente),
    path('doar/unica/', doarunica),
]
