import datetime

from usuarios.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, DateField
from django import forms
from app_site.models import Reserva, Sala_reuniones
from django.contrib.admin import widgets
from django.forms.widgets import Select, Widget
from django.forms.extras import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget

class RegistroForm (UserCreationForm):

	class Meta:
		model= User
		fields= [
			'username',
			'rut',
			'direccion',
			'tlf_movil',
			'first_name',
			'last_name',
			'email']
		labels= {'username': 'Nombre de Usuario',
				 'rut': 'Documento de identificacion',
				 'direccion': 'lugar o cosa donde vive',
				 'tlf_movil': 'tlf movil',
				 'first_name': 'Nombre',
				 'last_name': 'Apellidos',
				 'email': 'Correo',
				 
				 }
		widgets={'username': forms.TextInput(attrs={'class':'form-control'}),
				 'rut': forms.TextInput(attrs={'class':'form-control'}),
				 'direccion': forms.TextInput(attrs={'class':'form-control'}),
				 'tlf_movil': forms.TextInput(attrs={'class':'form-control'}),
				 'first_name':  forms.TextInput(attrs={'class':'form-control'}),
				 'last_name': forms.TextInput(attrs={'class':'form-control'}),
				 'email': forms.TextInput(attrs={'class':'form-control'}),
				 'password': forms.TextInput(attrs={'class':'form-control'}),
				 
				 }

class reservaForm (forms.ModelForm):
	#fecha = DateField(input_formats=['%d-%m-%Y'])
	class Meta:
		model= Reserva
		fields= [
			'fecha',
			'hora_inicio',
			'hora_termino',
			'cantidad_personas',
			'estado',
			'sala',
			]
		labels= {'fecha': 'Fecha de la reserva',
				 'hora_inicio': 'Hora inicio',
				 'hora_termino': 'Hora fin',
				 'cantidad_personas': 'Cantidad de personas',
				 'sala': 'Salas disponibles',
				 }
		widgets={'fecha': forms.DateInput(),
				 'hora_inicio': forms.TimeInput(attrs={'class':'form-control'}),
				 'hora_termino': forms.TimeInput(attrs={'class':'form-control'}),
				 'cantidad_personas':  forms.NumberInput(attrs={'class':'form-control'}),
				 'sala': forms.Select(attrs={'class':'form-control'}),
				 }
	def __init__(self, **kwargs):
		super(reservaForm, self).__init__(**kwargs)
		self.fields['sala'].queryset = Sala_reuniones.objects.exclude(estados='Confirmada')
		for field in iter(self.fields):
			if field <> 'estado':
				self.fields[field].widget.attrs.update({'class': 'form-control'})
				
