from django.db import models

class PlatoPrincipal(models.Model):
	Descripcion = models.CharField(max_length=30)
	Ingredientes = models.CharField(max_length=50)

	def __unicode__ (self):
		return str(self.Descripcion)


class Guarnicion(models.Model):
	Descripcion = models.CharField(max_length=30)
	Ingredientes = models.CharField(max_length=50)

	def __unicode__ (self):
		return str(self.Descripcion)


class Postre(models.Model):
	Descripcion = models.CharField(max_length=30)

	def __unicode__ (self):
		return str(self.Descripcion)


class Comida(models.Model):
	Comida_id = models.AutoField(primary_key=True)
	C_Ppal = models.ForeignKey(PlatoPrincipal)
	C_Guarnicion = models.ForeignKey(Guarnicion)
	C_Postre  = models.ForeignKey(Postre)

	def __unicode__ (self):
		return str(self.C_Ppal)

