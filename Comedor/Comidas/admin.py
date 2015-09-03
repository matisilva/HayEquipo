from django.contrib import admin
from .models import Comidas
# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display = ('Nombre','Precio','Descripcion')

admin.site.register(Comidas, UserAdmin)
