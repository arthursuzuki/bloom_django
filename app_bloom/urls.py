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
    path('feedbackpadrinho',views.feedbackpadrinho, name='feedbackpadrinho'),
    path('finishfeedback',views.finishfeedback,name='finishfeedback'),
    path('cadastropadrinho', views.cadastropadrinho, name='cadastropadrinho'),
    path('desenvolvimento',views.desenvolvimentopadri,name='desenvolvimento'),
    path('albumrecordacoesespecifico/<int:crianca_id>/', views.albumderecordacoesepecificio, name='albumrecordacoesespecifico'),
    path('menucriancafunci/<int:crianca_id>/', views.menucriancafunci, name='menucriancafunci'),
    path('menucriancafunciold', views.menucriancafunciold, name='menucriancafunciold'),
    path('desenvolvimentofunci', views.desenvolvimentofunci, name='desenvolvimentofunci'),
    path('album_recordacoes/<int:crianca_id>/', views.albumrecordacoes, name='albumrecordacoesnew'),
    path('albumrecordacoes/',views.albumderecordacoesold,name='albumrecordacoes'),
    path('eumanha', views.eumanha, name='eumanha'),
    path('menuchamada', views.menuchamada, name='menuchamada'),
    path('fimchamada', views.fimchamada, name='fimchamada'),
    path('eutarde', views.eutarde, name='eutarde'),
    path('nosmanha', views.nosmanha, name='nosmanha'),
    path('nostarde', views.nostarde, name='nostarde'),
    path('fomr',views.create_recordacao,name='createrecordacao')
]


