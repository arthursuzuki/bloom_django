from django.urls import path,include
from django.http import HttpResponse
from app_bloom.views import *


urlpatterns = [
    path('',home_page),
    path('hello/',home_page,name="name"),
    path('sobre/',home_page,name="sobre"),
    path('login/padrinho/',home_page,name="l_padrinho"),
    path('contribuir/',home_page,name="contribuir"),
    path('logins/',home_page,name="opc_login")
]
