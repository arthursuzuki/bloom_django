from django.shortcuts import render

from .forms import CriancaForm


def menu(request):
    return render(request, 'menu.html', context={
        'name': 'Menu'
    })


def sobre(request):
    return render(request, 'header.html', context={
        'name': 'Sobre'
    })


def padrinho(request):
    return render(request, 'header.html', context={
        'name': 'Padrinho'
    })


def doar(request):
    return render(request, 'doar.html', context={
        'name': 'Contribuições'
    })


def doarRecorrente(request):
    return render(request, 'doarrecorrente.html', context={
        'name': 'Contribuições'
    })


def doarUnica(request):
    return render(request, 'doarunica.html', context={
        'name': 'Contribuições'
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


def loginFunci(request):
    return render(request, 'login_funci.html', context={
        'name': 'Login Funcionário'
    })


def login(request):
    return render(request, 'login.html', context={
        'name': 'Login'
    })
