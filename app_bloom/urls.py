from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu, name="home"),
    path('sobre', views.sobre, name="sobre"),
    path('padrinho', views.padrinho, name="padrinho"),
    path('criancas', views.criancas, name="criancas"),
    path('menucrianca1', views.menucrianca1, name="menucrianca1"),
    path('menucrianca2', views.menucrianca2, name="menucrianca2"),
    path('loginpadri', views.loginpadri, name="loginpadri"),
    path('cadastrocrianca', views.cadastroCrianca, name="cadastrar_crianca"),
    path('loginfunci', views.loginfunci, name='loginfunci'),
    path('funcionario', views.funcionario, name='funcionario'),
    path('selecionar', views.selecionar, name='selecionar'),
    path('desenvolvimentofunci', views.desenvolvimentofunci, name='desenvolvimentofunci'),
    path('menualterar', views.menualterar, name='menualterar'),
]
