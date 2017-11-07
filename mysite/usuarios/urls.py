from django.conf.urls import url
from django.contrib import admin
from usuarios.views import RegistroUsuario, index, base, Inicio, RegistroReserva

urlpatterns = [

   #Registro de usuarios
   url(r'^base/', base),
   url(r'^inicio/', Inicio),
   url(r'^registro/',RegistroUsuario.as_view(), name= "registrar_user"),
   url(r'^reserva/',RegistroReserva.as_view(), name= "registrar_reserva"),
]
