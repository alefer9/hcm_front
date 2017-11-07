# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from usuarios.forms import RegistroForm, reservaForm
from django.http import HttpResponseRedirect
from app_site.models import Reserva, Solicitud, Sala_reuniones
#Clase que permite el registro de usuario
class RegistroUsuario(CreateView):
	model= User
	template_name= "usuarios/registrar.html"
	form_class= RegistroForm
	success_url = 'admin_inicio'
#Clase que permite el Registro de las reserva por los usuarios
class RegistroReserva(CreateView):
	model= Reserva
	template_name= "usuarios/reservar.html"
	form_class= reservaForm
	success_url = '/index/inicio/'
	
	def form_valid(self, form):
		empleado = self.request.user
		form.empleado = empleado
		solicitud = Solicitud()
		if form.is_valid():
			ok = form.save()
			ok_2 = Solicitud.objects.create(empleado=empleado, reserva=ok)
			return super(RegistroReserva, self).form_valid(form)


       
def index(request):
	return render_to_response("usuarios/index.html")

def base(request):
    return render(request, 'base/base.html')

def Inicio(request):
    return render(request, 'usuarios/inicio.html')


class ReservasUpdateView(UpdateView):
    form_class = reservaForm
    model = Reserva
    template_name = 'app_site/editar_reserva.html'
    success_url = '/app_site/inicio'
    def form_valid(self, form):
    	if form.is_valid():
    		ok = form.save()
    		if ok.estado == 'Confirmada':
    			ok_2 = Sala_reuniones.objects.filter(id = ok.sala.pk).update(estados = 'No disponible')
    			reserva_lista = Reserva.objects.filter(sala = ok.sala.pk, estado = 'Reservada').delete()
    			return render(self.request, 'app_site/listar_reservas.html')
    		else:
    			return render(self.request, 'app_site/listar_reservas.html')
    	# if form.cleaned_data['estado'] == 'Confirmada':
    	# 	# sala = Sala_reuniones.objects.get(form.cleaned_data['sala_id'])
    	# 	# sala.estados = 'No disponible'
    	# 	# sala.save()
    	# 	print("entro")
    	return render(self.request, 'usuarios/inicio.html')
    	# else:
    	# 	return render(request, 'usuarios/inicio.html')

class ReservasDelete(DeleteView):
    model = Reserva
    success_url = '/app_site/inicio'
    template_name = 'app_site/eliminar_reserva.html'