from django.db import models

class Personal(models.Model):
    nombe = models.CharField(max_length=75)
    apellido = models.CharField(max_length=75)
    telefono = models.CharField(max_length=12)
    fecha_nacimiento = models.DateField()
    codigo = models.IntegerField()