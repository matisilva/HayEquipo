from django.db import models
#Importo los modelos de las otras apps
from Usuarios.models import Usuario
from Comidas.models import Comida

#Objetivo: definir asistencia a comer,
class Asistencia(models.Model):
    A_usuario = models.ForeignKey(Usuario)
    A_menu = models.ForeignKey(Comida)
    A_fecha = models.DateTimeField(auto_now_add = True)
    A_id = models.AutoField(primary_key=True)

