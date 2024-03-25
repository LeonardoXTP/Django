from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('miembros/', views.miembros, name='miembros'),
    path('miembros/detalles/<int:id>/', views.detalles, name='detalles'),
    path('prueba/', views.prueba, name='prueba'),
]