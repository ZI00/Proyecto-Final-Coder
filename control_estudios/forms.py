from django import forms

class CursoFormulario(forms.Form):
    Nombre = forms.CharField(required=True, max_length=70)
    Edad = forms.IntegerField(required=True, max_value=120)
