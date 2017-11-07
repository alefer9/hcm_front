# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from usuarios.models import User

class Insumos (models.Model):
	descripcion = models.CharField(max_length=45)
	def __unicode__(self):
		return '%s' % (self.descripcion)

class Sala_reuniones (models.Model):

	NODISPONIBLE = 'No Disponible'
	DISPONIBLE = 'Disponible'
	RESERVADA = 'Reservada'
	CONFIRMADA = 'Confirmada'
	ESTADO_CHOICES = (
        (NODISPONIBLE, 1),
        (DISPONIBLE, 2),
        (RESERVADA, 3),
        (CONFIRMADA, 4),
    )
	
	nombre= models.CharField(max_length=45)
	ubicacion= models.CharField(max_length=45, null=True, blank=True)
	capacidad= models.IntegerField()
	horario_disponible= models.DateTimeField(max_length=45, null=True, blank=True)
	estados= models.CharField(max_length=10,choices=ESTADO_CHOICES,default=DISPONIBLE,)
	
	insumos = models.ManyToManyField(Insumos, through='Sala_reuniones_insumos', related_name='%(class)s_requests_created')

	def __unicode__(self):
		return '%s' % (self.nombre)

class Reserva (models.Model):
	RESERVADA= 'Reservada'
	CONFIRMADA = 'Confirmada'
	ESTADO_CHOICES = (
		(RESERVADA, 'Reservada'),
		(CONFIRMADA, 'Confirmada'),)
	fecha = models.DateField(max_length=45)
	hora_inicio = models.TimeField(max_length=45)
	hora_termino= models.TimeField(max_length=45)
	cantidad_personas = models.CharField(max_length=45)
	estado=models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default=RESERVADA)
	sala = models.ForeignKey(Sala_reuniones, on_delete=models.CASCADE)
	empleado = models.ManyToManyField(User, through='Solicitud', related_name='%(class)s_requests_created')
	
	def __unicode__(self):
		return '%s %s %s %s %s' % (self.estado, self.fecha, self.hora_inicio, self.hora_termino, self.cantidad_personas)

class Solicitud(models.Model):
	empleado = models.ForeignKey(User,on_delete=models.CASCADE)
	reserva= models.ForeignKey(Reserva,on_delete=models.CASCADE)
	class Meta:
		auto_created =True
	def __unicode__(self):
		return ' %s %s' % (self.empleado, self.reserva)

class Sala_reuniones_insumos(models.Model):
	sala_reuniones = models.ForeignKey(Sala_reuniones,on_delete=models.CASCADE,null=True,related_name='%(class)s_requests_created')
	insumos = models.ForeignKey(Insumos,on_delete=models.CASCADE,null=True)
	class Meta:
		auto_created =True
	def __unicode__(self):
		return ' %s %s' % (self.sala_reuniones, self.insumos)

