from django.contrib import admin
from .models import Asistencia
# Register your models here.
class AsistenciaAdmin(admin.ModelAdmin):
	list_display = ('A_id', 'A_usuario', 'A_menu', 'A_fecha')

admin.site.register(Asistencia, AsistenciaAdmin)
