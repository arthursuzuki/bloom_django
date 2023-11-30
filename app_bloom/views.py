from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from .forms import *
from .models import DadosCrianca


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
    criancas = Crianca.objects.all()
    context = {'criancas': criancas}
    return render(request, 'selecionar.html', context)


def menualterar(request):
    return render(request, 'menualterar.html', context={
        'name': 'Alterar Menu'
    })

def cadastropadrinho(request):
    return render(request, 'cadastropadrinho.html', context={
        'name': 'Cadastro Padrinho'
    })


def desenvolvimentofunci(request):
    crianca = Crianca.objects.get(pk=crianca_id)
    if request.method == 'POST':
        mes = request.POST.get('mes')
        atividade = request.POST.get('atividade_secao1')
        carga_horaria = request.POST.get('carga')
        desempenho = request.POST.get('desempenho_secao1')

        # Salvar no banco de dados
        DadosCrianca.objects.create(
            mes=mes,
            atividade=atividade,
            carga_horaria=carga_horaria,
            desempenho=desempenho
        )

        return redirect('desenvolvimentofunci',{'crianca': crianca})  # Redirecione para a página de sucesso

    return render(request, 'desenvolvimentofunci.html')


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
        form = CadastroCriancaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success_message = "Os dados foram enviados com sucesso!"
    else:
        form = CadastroCriancaForm()
    return render(request, 'cadastrocrianca.html', {
        'form': form,
        'success_message': success_message,
        'name': 'Cadastro'
        })


def finishfeedback(request):
    return render(request,'finishfeedback.html')

def albumderecordacoes(request):
    recordacoes = recordacoes.objects.all()

    # Divida os registros em grupos de 5
    records_por_pagina = 5
    paginas = [recordacoes[i:i + records_por_pagina] for i in range(0, len(recordacoes), records_por_pagina)]

    # Obtenha o número da página da consulta GET (se disponível)
    page = request.GET.get('page', 1)

    # Se a página for maior que o número total de páginas, retorne a última página
    try:
        current_page = paginas[int(page) - 1]
    except IndexError:
        current_page = paginas[-1]

    return render(request, 'desenvolvimento.html', {'recordacoes': current_page})

def albumderecordacoesepecificio(request):
    crianca = get_object_or_404(Recordacoes, pk=cpf)

    return render(request, 'album_foto_especifica.html', {'crianca': crianca})

def menucriancafunci(request, crianca_id):
    crianca = Crianca.objects.get(pk=crianca_id)
    return render(request, 'menucriancafuncionario.html', {'crianca': crianca})
