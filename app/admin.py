from django.contrib import admin
from .models import Marca, Producto, Contacto

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "nuevo", "marca"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_per_page = 5

class ContactoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "correo", "tipo_consulta", "avisos"]
    list_editable = ["correo","avisos"]
    search_fields = ["nombre", "correo"]
    list_per_page = 10




admin.site.register(Marca)
admin.site.register(Producto, ProductAdmin)
admin.site.register(Contacto, ContactoAdmin)


