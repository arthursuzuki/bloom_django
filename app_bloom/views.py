from django.shortcuts import render,redirect
from django.http import JsonResponse
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


def recordacoes(request):
    return render(request, 'recordacoes.html', context={
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

def cadastropadrinho(request):
    return render(request, 'cadastropadrinho.html', context={
        'name': 'Cadastro Padrinho'
    })


def desenvolvimentofunci(request):
    return render(request, 'desenvolvimentofunci.html', context={
        'name': 'Alterar Desenvolvimento'
    })
def desenvolvimentopadri(request):
    itens = Atividades.objects.all()
    
    # Aplicar filtros se o formulário for enviado
    if request.method == 'GET':
        form = AtividadesForm(request.GET)
        if form.is_valid():
            mes = form.cleaned_data.get('mes')
            atividade = form.cleaned_data.get('atividade')
            carga_horaria = form.cleaned_data.get('carga_horaria')
            avaliacao_red = form.cleaned_data.get('avaliacao_red')
            avaliacao_yellow = form.cleaned_data.get('avaliacao_yellow')
            avaliacao_green = form.cleaned_data.get('avaliacao_green')

            # Aplicar filtros ao queryset
            if mes:
                itens = itens.filter(mes__icontains=mes)
            if atividade:
                itens = itens.filter(atividade__icontains=atividade)
            if carga_horaria:
                itens = itens.filter(carga_horaria__gte=carga_horaria)
            if avaliacao_red:
                itens = itens.filter(avaliacao_red__lte=avaliacao_red)
            if avaliacao_yellow:
                itens = itens.filter(avaliacao_yellow__lte=avaliacao_yellow)
            if avaliacao_green:
                itens = itens.filter(avaliacao_green__lte=avaliacao_green)

    else:
        form = AtividadesForm()

    # Retornar dados JSON para atualização assíncrona
    data = {
        'itens': [{'mes': item.mes, 'atividade': item.atividade, 'carga_horaria': item.carga_horaria,
                   'avaliacao_red': item.avaliacao_red, 'avaliacao_yellow': item.avaliacao_yellow,
                   'avaliacao_green': item.avaliacao_green} for item in itens]
    }

    return render(request, 'desenvolvimento.html', {'itens': itens, 'form': form, 'data': data})

def feedbackpadrinho(request):
    if request.method == 'POST':
        form =  FeedbackPadrinhoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finishfeedback')

            
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


def finishfeedback(request):
    return render(request,'finishfeedback.html')

def albumderecordacoes(request):
    recordacoes = Recordacoes.objects.all()
    return render(request, 'albumderecordacoes.html', {'recordacoes': recordacoes})


def albumderecordacoes(request):
    recordacoes = Recordacoes.objects.all()
    return render(request, 'album_foto_especifica.html', {'recordacoes': recordacoes})

