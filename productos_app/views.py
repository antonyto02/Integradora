from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def menu_principal(request):
    return render(request, 'productos_app/menu_principal.html')

@login_required
def productos(request):
    return render(request, 'productos_app/productos.html')

@login_required
def proveedores(request):
    return render(request, 'productos_app/proveedores.html')

@login_required
def empleados(request):
    return render(request, 'productos_app/empleados.html')
