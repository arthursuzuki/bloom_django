from django import forms
from AppBloom.models import Crianca


class CriancaForm(forms.ModelForm):
    class Meta:
        model = Crianca
        fields = '__all__'
