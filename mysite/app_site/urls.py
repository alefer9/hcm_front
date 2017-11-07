from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from .views import RegistroSalas,  RegistroInsumos, ListarSalas, ListarInsumos, ListarReservas, Inicio
from usuarios.views import ReservasUpdateView , ReservasDelete

urlpatterns = [

   #Pagina Principal de la app
   url(r'^registro/salas',RegistroSalas.as_view(), name= "registrar_salas"),
   url(r'^registro/insumos',RegistroInsumos.as_view(), name= "registrar_insumos"),
   url(r'^listar/salas',ListarSalas.as_view(), name= "listar_salas"),
   url(r'^listar/insumos',ListarInsumos.as_view(), name= "listar_insumos"),
   url(r'^inicio',Inicio, name= "admin_inicio"),
   url(r'^listar/reservas',ListarReservas, name= "listar_reservas"),
   url(r'^editar/reservas/(?P<pk>[\w-]+)$',ReservasUpdateView.as_view(), name= "editar_reservas"),
   url(r'^eliminar/reservas/(?P<pk>[\w-]+)$',ReservasDelete.as_view(), name= "eliminar_reservas"),
   #url(r'^listar/solicitudes',ListarSolicitud.as_view(), name= "listar_solicitudes"),
]
