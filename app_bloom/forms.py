from django import forms
from app_bloom.models import *


class CriancaForm(forms.ModelForm):
    class Meta:
        model = Crianca
        fields = '__all__'

class FeedbackPadrinhoForm(forms.ModelForm):
    class Meta:
        model = FeedbackPadrinho
        fields = '__all__'

class formLogin(forms.ModelForm):
    class Meta:
        model = Login
        fields = [
            'cpf',
            'senha'
        ]