from django import forms
from django.core.validators import RegexValidator
from .models import Musico, Grupo

class AddFormMusico(forms.ModelForm):

    class Meta:
        model = Musico
        fields = [
            'nombre',
            'fec_nacimiento',
            'instrumento',
        ]
        
        widgets = {
            'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
            'fec_nacimiento' : forms.DateInput(attrs={'class' : 'form-control'}),
            'instrumento' : forms.Select(attrs={'class' : 'form-control'}),
        }

class AddFormGrupo(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = [
            'nombre', 
            'fec_fundacion',
            'estilo',
            'miembros',
        ]
        
        widgets = {
            'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
            'fec_fundacion' : forms.DateInput(attrs={'class' : 'form-control'}),
            'estilo' : forms.Select(attrs={'class' : 'form-control'}),
            'miembros' : forms.CheckboxSelectMultiple(),
        } 