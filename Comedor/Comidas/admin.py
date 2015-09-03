from django.contrib import admin
from .models import Comida
# Register your models here.

class ComidaAdmin(admin.ModelAdmin):
	list_display = ('Nombre','Precio','Descripcion')

admin.site.register(Comida, ComidaAdmin)
