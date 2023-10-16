from django.shortcuts import render
# from AppBloom.models import Crianca
from AppBloom.forms import CriancaForm
# from django.http import HttpResponse


# Create your views here.
def home(request):
    success_message = None
    if request.method == 'POST':
        form = CriancaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Aceito")
            success_message = "Os dados foram enviados com sucesso!"
    else:
        print("Erro ao salvar os dados")
        form = CriancaForm()
    return render(request, 'cadastroCrianca.html', {'form': form, 'success_message': success_message})
