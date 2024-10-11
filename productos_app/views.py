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
                {"opcion": "MOSTRAR TODO", "link": "https://i.postimg.cc/W4nM5tBk/seleccionar-todo-1.png"},
                {"opcion": "LIMPIEZA", "link": "https://i.postimg.cc/vHrWxFgS/productos.png"},
                {"opcion": "INSUMOS", "link": "https://i.postimg.cc/qBcLyTyC/comida-1.png"},
                {"opcion": "DESECHABLES", "link": "https://i.postimg.cc/qq2s49Hn/contenedor-de-comida.png"},
                {"opcion": "LOZA", "link": "https://i.postimg.cc/tg6nZJ56/vajilla.png"},

            ]
        }
        
    elif categoria=="empleados":
        context = {
            "opciones": [
                {"opcion": "MOSTRAR TODO", "link": "https://i.postimg.cc/W4nM5tBk/seleccionar-todo-1.png"},
                {"opcion": "COCINA", "link": "https://i.postimg.cc/6QnJcnb6/camarero.png"},
                {"opcion": "MESERO", "link": "link3"},
                {"opcion": "RH", "link": "link4"},
                {"opcion": "RECEPCIONISTA", "link": "link5"},

            ]
        }
        
    return render(request, 'productos_app/submenus.html', context)

@login_required
def proveedores(request):
    pass