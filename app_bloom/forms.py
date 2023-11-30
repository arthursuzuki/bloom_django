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


class AtividadesForm(forms.ModelForm):
    class Meta:
        model = Atividades
        fields = ['mes']

class CadastroCriancaForm(forms.ModelForm):
    class Meta:
        model = Crianca
        fields = '__all__'


class SelecionarTelaForm(forms.ModelForm):
    class Meta:
        model = Crianca
        fields = ['nome']


class PadrinhoForm(forms.ModelForm):
    class Meta:
        model = Padrinho
        fields = ['nome', 'telefone', 'endereco', 'cpf', 'email', 'rg', 'profissao', 'reason']

    nomeCompleto = forms.CharField(label='Nome Completo', widget=forms.TextInput(attrs={'class': 'form-control-sm'}))
    telefone = forms.CharField(label='Número de Telefone', widget=forms.TextInput(attrs={'class': 'form-control-sm', 'type': 'tel'}))
    endereco = forms.CharField(label='Endereço', widget=forms.TextInput(attrs={'class': 'form-control-sm'}))
    cpf = forms.CharField(label='CPF', widget=forms.TextInput(attrs={'class': 'form-control-sm'}))
    email = forms.EmailField(label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control-sm', 'type': 'email'}))
    rg = forms.CharField(label='RG', widget=forms.TextInput(attrs={'class': 'form-control-sm'}))
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control-sm'}))
    profissao = forms.CharField(label='Profissão', widget=forms.TextInput(attrs={'class': 'form-control-sm'}))
    motivoCadastro = forms.CharField(label='Motivo do Cadastro', widget=forms.TextInput(attrs={'class': 'form-control-sm'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['motivoCadastro'].widget.attrs['class'] = 'form-control-sm'
        self.fields['motivoCadastro'].widget.attrs['id'] = 'motivoCadastro'
