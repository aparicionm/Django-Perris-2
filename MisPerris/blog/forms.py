from django import forms

from .models import Rescatado

class ResForm(forms.ModelForm):

    class Meta:
        model = Rescatado
        fields = ('foto','nombre', 'raza','descripcion','estado')
