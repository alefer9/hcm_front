from .models import Sala_reuniones, Insumos
from django.forms import ModelForm
from django import forms


class salasForm (ModelForm):

	class Meta:
		model= Sala_reuniones
		NODISPONIBLE = 'ND'
		DISPONIBLE = 'D'
		RESERVADA = 'R'
		CONFIRMADA = 'C'
		ESTADO_CHOICES = (
			(NODISPONIBLE, 'Nodisponible'),
			(DISPONIBLE, 'Disponible'),
			(RESERVADA, 'Reservada'),
			(CONFIRMADA, 'Confirmada'),)
	
		fields= [
			'nombre',
			'ubicacion',
			'capacidad',
			'horario_disponible',
			'estados',
			'insumos',
			]
		labels= {'nombre': 'Nombre de Sala',
				 'ubicacion': 'Ubicacion de Sala',
				 'capacidad': 'Cantidad de Personas',
				 'horario_disponible': 'Horario de la sala',
				 'estados': 'Estados',
				 'insumos': 'Insumos',
				 }
		widgets={'nombre': forms.TextInput(attrs={'class':'form-control'}),
				 'ubicacion': forms.TextInput(attrs={'class':'form-control'}),
				 'capacidad': forms.TextInput(attrs={'class':'form-control'}),
				 'horario_disponible':  forms.DateInput(format='%d/%m/%Y'),
				 'estados': forms.TextInput(attrs={'class':'form-control'}),
				 'insumos': forms.CheckboxSelectMultiple(),
				 }
		

class insumosForm (ModelForm):

	class Meta:
		model= Insumos
	
		fields= [
			'descripcion',
			]
		labels= {'descripcion': 'Nombre del insumo',
				 }
		widgets={'descripcion': forms.TextInput(attrs={'class':'form-control'}),
				 }



