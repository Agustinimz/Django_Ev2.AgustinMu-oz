from datetime import datetime
from tkinter.tix import InputOnly
from django import forms
from django.forms import TimeInput
from reservas_App.models import reserva

class FormReserva(forms.ModelForm):
    
    nombre = forms.CharField(label='Nombre', min_length=5, max_length=20)
    telefono = forms.CharField(min_length=9, max_length=9)
    fecha = forms.DateField(widget= forms.SelectDateWidget)
    hora = forms.CharField(label= 'Hora', min_length=5, max_length=5)
    cantidadPersonas = forms.IntegerField(label='Catidad de Personas', min_value=1, max_value=15)
    Estados = [('completada', 'COMPLETADA'),('reservado', 'RESERVADO'),('anulada', 'ANULADA'),('no asisten', 'NO ASISTEN')] 
    estado = forms.CharField(widget=forms.Select(choices=Estados))
    observacion = forms.CharField(required=False)
    
    
    
    
    class Meta:
        model = reserva
        fields = '__all__'
        
        
    
    