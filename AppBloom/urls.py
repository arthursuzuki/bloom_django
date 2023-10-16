from django.urls import path
from AppBloom import views

urlpatterns = [
    path('', views.home, name='cadastrar_crianca'),
]
