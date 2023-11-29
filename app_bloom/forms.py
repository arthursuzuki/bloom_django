from django import forms
from app_bloom.models import *


class CriancaForm(forms.ModelForm):
    class Meta:
        model = Crianca
        fields = '__all__'


class FeedbackPadrinhoForm(forms.ModelForm):
    class Meta:
        model = FeedbackPadrinho
        fields = ['nome','destinatario','mensagem']

from django import forms
from .models import Padrinho

class LoginPadrinhoForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Padrinho
        fields = ['cpf', 'senha']

    def clean(self):
        cleaned_data = super().clean()
        cpf = cleaned_data.get('cpf')
        senha = cleaned_data.get('senha')

        # Chama a função para validar as credenciais
        if not self.validar_credenciais(cpf, senha):
            raise forms.ValidationError("Credenciais inválidas. Por favor, verifique seu CPF e senha.")

    def validar_credenciais(self, cpf, senha):
        # Adicione a lógica para verificar as credenciais no banco de dados
        try:
            padrinho = Padrinho.objects.get(cpf=cpf, senha=senha)
            return True
        except Padrinho.DoesNotExist:
            return False

class ItemFilterForm(forms.Form):
    nome = forms.CharField(required=False)
    destinatario = forms.DecimalField(required=False, min_value=0)
    mensagem = forms.DecimalField(required=False, min_value=0)