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

############################################################
def sintaxis (request):
    misusers = Usuario.objects.all().values()
    template = loader.get_template('sintaxis.html')
    context = {
        'misusers': misusers,
        'bienvenida': 1,
        'animales': ['perro', 'gato'],
        'x': ['manzana', 'pera', 'uva'],
        'y': ['manzana', 'pera', 'uva'],
        
        'coches': [
            {
                'id': 1,
                'marca': 'Lamborghini',
                'modelo': 'Veneno',
                'año': '2019',
            },
            {
                'id': 2,
                'marca': 'Ferrari',
                'modelo': 'La Ferrari',
                'año': '2021',
            },
            {
                'id': 3,
                'marca': 'Ford',
                'modelo': 'Mustang',
                'año': '2023',
            }
        ],

        'objetovacio': [],
        'colores': ['rojo','verde', 'azul'],
    }
    return HttpResponse(template.render(context, request))

############################################################

def consulta (request):
    misdatos = Usuario.objects.all()
    template = loader.get_template('consultas.html')
    context = {
        'misdatos': misdatos,
    }
    return HttpResponse(template.render(context, request))

def conjuntos (request):
    # values() permite devolver cada objeto como un diccionario de Python

    misdatos = Usuario.objects.all()._list('nombre') # Devuelve la columna de nombre

    # misdatos = Usuario.objectsfilter(nombre='Leonardo', id=1).values() --> Filtro

    # Usuario.objects.filter(nombre='Mateo').values() | Usuario.objects.filter(firstname='Maria').values() --> x "o" y

    # from django.db.models import Q

    # Usuario.objects.filter(Q(nombre='Mateo') | Q(firstname='Maria')).values() --> filtrar importando Q

    # Usuario.objects.filter(nombre='L').values() --> Filtrar por un caracter

    # Usuario..objects.all().order_by('nombre').values() --> Ordenar por

    # Usuario.objects.all().order_by('nombre').values() --> Orden descendente

    # Usuario.objects.all().order_by('apelldo', 'id').values() --> Ordenar por más de un campo

    template = loader.get_template('consultas.html')
    context = {
        'misdatos': misdatos,
    }
    return HttpResponse(template.   render(context, request))