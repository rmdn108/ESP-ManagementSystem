from django import forms
from .models import Module

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['departement', 'intitule', 'coef', 'nombre_credit', 'volume_horaires_cm', 'volume_horaires_td', 'volume_horaires_tp', 'unite_enseignement', 'semestre', 'enseignant_responsable']
