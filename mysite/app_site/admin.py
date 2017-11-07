# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import admin
from usuarios.models import User 
from app_site.models import * 
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
 
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =   ('id','username','password','first_name','last_name',
'email','is_staff','is_active','is_superuser',
'last_login','date_joined')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display =   ('id','fecha','hora_inicio','hora_termino','cantidad_personas',
'estado')

@admin.register(Sala_reuniones)
class Sala_reunionesAdmin(admin.ModelAdmin):
    list_display =   ('id','nombre','ubicacion','capacidad','estados')

@admin.register(Insumos)
class InsumosAdmin(admin.ModelAdmin):
    list_display =   ('id','descripcion')

