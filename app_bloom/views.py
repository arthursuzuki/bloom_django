from django.shortcuts import render

from .forms import *


def menu(request):
    return render(request, 'menu.html', context={
        'name': 'Menu'
    })


def sobre(request):
    return render(request, 'header.html', context={
        'name': 'Sobre'
    })


def padrinho(request):
    return render(request, 'padrinho.html', context={
        'name': 'Padrinho'
    })


def criancas(request):
    return render(request, 'criancas.html', context={
        'name': 'Menu Criança'
    })


def menucrianca1(request):
    return render(request, 'menucrianca1.html', context={
        'name': 'Menu Criança'
    })


def menucrianca2(request):
    return render(request, 'menucrianca2.html', context={
        'name': 'Menu Criança'
    })


def funcionario(request):
    return render(request, 'funcionario.html', context={
        'name': 'Funcionário'
    })


def cadastroCrianca(request):
    success_message = None
    if request.method == 'POST':
        form = CriancaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success_message = "Os dados foram enviados com sucesso!"
    else:
        form = CriancaForm()
    return render(request, 'cadastrocrianca.html', {
        'form': form,
        'success_message': success_message,
        'name': 'Cadastro'
        })


def loginfunci(request):
    return render(request, 'loginfunci.html', context={
        'name': 'Login Funcionário'
    })


def loginpadri(request):
    return render(request, 'loginpadri.html', context={
        'name': 'Login Padrinho'
    })


def selecionar(request):
    return render(request, 'selecionar.html', context={
        'name': 'Selecionar Criança'
    })


def menualterar(request):
    return render(request, 'menualterar.html', context={
        'name': 'Alterar Menu'
    })


def desenvolvimentofunci(request):
    return render(request, 'desenvolvimentofunci.html', context={
        'name': 'Alterar Desenvolvimento'
    })


def feedbackpadrinho(request):
    if request.method == 'POST':
        form =  FeedbackPadrinhoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FeedbackPadrinhoForm()
    return render(request,"feedbackpadrinho.html",{'form':form})


def cadastroCrianca(request):
    success_message = None
    if request.method == 'POST':
        form = CriancaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success_message = "Os dados foram enviados com sucesso!"
    else:
        form = CriancaForm()
    return render(request, 'cadastrocrianca.html', {
        'form': form,
        'success_message': success_message,
        'name': 'Cadastro'
        })
