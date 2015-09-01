from django.db import models

# Create your models here.

class Usuarios(models.Model):
	Nombre = models.CharField(max_length=60)
	Apellido = models.CharField(max_length=60)
	Dni = models.IntegerField()
	User_id = models.AutoField(primary_key=True)
	Telefono = models.IntegerField()
	Nacimiento = models.DateField()
	
	def __unicode__(self):
	        return self.Nombre
		return self.Apellido
