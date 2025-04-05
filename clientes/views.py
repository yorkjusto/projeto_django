from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lista_clientes(request):
    return render(request, 'lista.html')

def criar_cliente(request):
    return render(request, 'criar.html')

def editar_cliente(request):
    return render(request, 'editar.html')

def remover_cliente(request):
    return render(request, 'remover.html')

def consultar_cliente(request):
    return render(request, 'consultar.html')


