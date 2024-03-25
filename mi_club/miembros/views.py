from django.http import HttpResponse
from django.template import loader
from .models import Usuario

def miembros (request):
    usuarios = Usuario.objects.all().values()
    template = loader.get_template('lista.html')
    context = {
        'usuarios': usuarios
    }
    return HttpResponse(template.render(context, request))

def detalles (request, id):
    usuarios = Usuario.objects.get(id=id)
    template = loader.get_template('detalles.html')
    context = {
        'usuarios': usuarios
    }
    return HttpResponse(template.render(context, request))

def inicio (request):
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render())

def prueba (request):
    template = loader.get_template('prueba.html')
    context = {
        'frutas': ['manzana', 'pera', 'uva'],
    }
    return HttpResponse(template.render(context, request))