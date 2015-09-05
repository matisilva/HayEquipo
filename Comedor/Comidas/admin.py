from django.contrib import admin
from .models import Comida,PlatoPrincipal,Postre,Guarnicion
# Register your models here.

class ComidaAdmin(admin.ModelAdmin):
	list_display = ('Comida_id','C_Ppal','C_Guarnicion','C_Postre')

class PpalAdmin(admin.ModelAdmin):
	list_display = ('Descripcion','Ingredientes')

class GAdmin(admin.ModelAdmin):
	list_display = ('Descripcion','Ingredientes')

class PostreAdmin(admin.ModelAdmin):
	list_display = ('Descripcion',)


#Agregado de control de admin y relacion de parametros
admin.site.register(PlatoPrincipal, PpalAdmin)
admin.site.register(Guarnicion, GAdmin)
admin.site.register(Postre, PostreAdmin)
admin.site.register(Comida, ComidaAdmin)

