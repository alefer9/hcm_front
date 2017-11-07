# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import CreateView, ListView
from django.template import RequestContext
from app_site.forms import salasForm, insumosForm
from .models import Sala_reuniones, Insumos, Reserva

#Clase que permite el registro de Salas de reuniones
class RegistroSalas(CreateView):
	model= Sala_reuniones
	template_name= "app_site/salareuniones.html"
	form_class= salasForm
	success_url = 'app_site/listar/salas'
#Clase que permite el registro de insumos
class RegistroInsumos(CreateView):
	model= Insumos
	template_name= "app_site/registroinsumos.html"
	form_class= insumosForm
	success_url = '/app_site/inicio'
#Clase que permite listar salas
class ListarSalas(ListView):
	model= Sala_reuniones
	template_name= "app_site/lista_salareuniones.html"
	def get_context_data(self, **kwargs):
		context = super(ListarSalas, self).get_context_data(**kwargs)
		return context
#Clase que permite listar Insumos
class ListarInsumos(ListView):
	model= Insumos
	template_name= "app_site/lista_insumos.html"
	def get_context_data(self, **kwargs):
		context = super(ListarInsumos, self).get_context_data(**kwargs)
		return context
#Funcion que permite listar las Reservas de las salas de reuniones
def ListarReservas(request):
   	reservas = Reserva.objects.all()
   	context = {"reservas":reservas}
   	return render(request, 'app_site/listar_reservas.html', context)
   	# return render_to_response('app_site/listar_reservas.html', context,context_instance=RequestContext(request))
# Funcion que muestra el inicio de la app
def Inicio(request):
    return render(request, 'app_site/index.html')





