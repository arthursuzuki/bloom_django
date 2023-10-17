from django.shortcuts import render
from django.http import HttpResponse
from app_bloom.urls import *
from app_bloom.forms import *

def home_page(request):
    return render(request,'inicial/header.html')
def menu(request):
    return render(request,'inicial/menu.html')
def login(request):
    return render(request,'inicial/login.html')
def doar (request):
    return render(request, 'inicial/doar.html')

def funcionario (request):
    return render(request, 'funcionario.html')

def doarrecorrente (request):
    return render(request, 'inicial/doarrecorrente.html')

def doarunica (request):
    return render(request, 'inicial/doarunica.html')
def cadastrocrianca(request):
    success_message = None
    if request.method == 'POST':
        form = CriancaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success_message = "Os dados foram enviados com sucesso!"
    else:
        form = CriancaForm()
    return render(request, 'inicial/cadastrocrianca.html', {'form': form, 'success_message': success_message})
def login_funci(request):
    return render(request,'inicial/login_funci.html')
def funcionario(request):
    return render(request, 'inicial/funcionario.html')
