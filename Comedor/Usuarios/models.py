from django.db import models

# Create your models here.

class Usuario(models.Model):
    #Defino las constantes y opciones
    ESTUDIANTE = 'ES'
    BECADO = 'BE'
    DOCENTE = 'DO'
    CONDITION_CHOICES = (
        (ESTUDIANTE,'Estudiante'),
        (BECADO,'Becado'),
        (DOCENTE,'Docente'),
    )

    Nombre = models.CharField(max_length=60)
    Apellido = models.CharField(max_length=60)
    Dni = models.IntegerField()
    User_id = models.AutoField(primary_key=True)
    Telefono = models.IntegerField()
    Nacimiento = models.DateField()
    Condicion = models.CharField(choices=CONDITION_CHOICES, max_length=20, default=ESTUDIANTE)
    Saldo = models.IntegerField(default = 0)

    def __unicode__(self):
        return str(self.Nombre) + str(self.Apellido)
