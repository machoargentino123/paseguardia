from datetime import date
from django import forms
from .models import Tablaseguimiento


class TktForm(forms.ModelForm):
    """Form definition for Tickets."""

    class Meta:
        """Meta definition for Tktform."""

        model = Tablaseguimiento

        fields = (
                   'detalle',
                   'reactivar',
                   'reactivar_hora',
                   'prioridad',      
                 )
        #ojo con la s de widgets!!!!!!
        widgets = {
            'prioridad': forms.CheckboxSelectMultiple(),
            'reactivar': forms.DateInput(),
            'reactivar_hora':forms.TimeInput(),
                  }   
        