from django.urls import path
from . import views

urlpatterns = [
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('criar_cliente/', views.criar_cliente, name='criar_cliente'),
    path('editar_cliente/', views.editar_cliente, name='editar_cliente'),
    path('remover_cliente/', views.remover_cliente, name='remover_cliente'),
    path('consultar_cliente/', views.consultar_cliente, name='consultar_cliente'),
]
