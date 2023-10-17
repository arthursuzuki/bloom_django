from django.urls import path,include
from django.http import HttpResponse
from app_bloom.views import *


urlpatterns = [
    path('',menu,name="home"),
    path('hello/',home_page,name="name"),
    path('sobre/',home_page,name="sobre"),
    path('login/padrinho/',home_page,name="l_padrinho"),
    path('contribuir/',home_page,name="contribuir"),
    path('logins/',login,name="opc_login"),
    path('doar/',doar,name='doar'),
    path('doar/recorrente/',doarrecorrente),
    path('doar/unica/', doarunica),
    path('cadastro/crianca/',cadastrocrianca,name="cadastrar_crianca"),
    path('login/funcionarios/',login_funci,name='loginfunc'),
    path('funcionario/', funcionario,name='funcionario'),
]
