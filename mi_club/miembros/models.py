from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    numero = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"