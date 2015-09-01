from django.contrib import admin
from .models import Usuarios
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('User_id', 'Nombre', 'Apellido', 'Dni', 'Nacimiento', 'Telefono')

admin.site.register(Usuarios, UserAdmin)
