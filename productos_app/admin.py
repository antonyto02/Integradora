from django.contrib import admin

from django.contrib import admin
from .models import Empleados, Proveedores, Categorias, Productos

# Registro de los modelos para que aparezcan en el panel de administración
admin.site.register(Empleados)
admin.site.register(Proveedores)
admin.site.register(Categorias)
admin.site.register(Productos)