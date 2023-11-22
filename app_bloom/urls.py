from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu, name="home"),
    path('sobre', views.sobre, name="sobre"),
    path('padrinho', views.padrinho, name="l_padrinho"),
    path('login', views.login, name="login"),
    path('doar', views.doar, name='doar'),
    path('recorrente/', views.doarRecorrente),
    path('unica/', views.doarUnica),
    path('cadastrocrianca', views.cadastroCrianca, name="cadastrar_crianca"),
    path('login/funcionario', views.loginFunci, name='login_funci'),
    path('funcionario', views.funcionario, name='funcionario'),
]
