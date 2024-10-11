from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def menu_principal(request):
    return render(request, 'productos_app/menu_principal.html')

@login_required
def submenus(request, categoria):
    context = {}

    if categoria == "productos":
        context = {
            "opciones": [
                {"opcion": "Mostrar todo", "link": "link1"},
                {"opcion": "Limpieza", "link": "link2"},
                {"opcion": "Insumos", "link": "link3"},
                {"opcion": "Desechables", "link": "link4"},
                {"opcion": "Loza", "link": "link5"},

            ]
        }
        
    elif categoria=="empleados":
        context = {
            "opciones": [
                {"opcion": "Mostrar todo", "link": "link1"},
                {"opcion": "Cocina", "link": "link2"},
                {"opcion": "Mesero", "link": "link3"},
                {"opcion": "RH", "link": "link4"},
                {"opcion": "Recepcionista", "link": "link5"},

            ]
        }
        
    return render(request, 'productos_app/submenus.html', context)

@login_required
def proveedores(request):
    pass