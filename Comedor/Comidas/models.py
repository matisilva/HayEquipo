from django.db import models
# Create your models here.
class Comidas(models.Model):
	Nombre = models.CharField(max_length=60)
	Precio = models.IntegerField()
	Descripcion = models.CharField(max_length=200)
