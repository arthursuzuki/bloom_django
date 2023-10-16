from django import forms
from app_bloom.models import Crianca


class CriancaForm(forms.ModelForm):
    class Meta:
        model = Crianca
        fields = '__all__'
