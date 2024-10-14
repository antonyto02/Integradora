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
                {"pantalla":"1","opcion": "MOSTRAR TODO", "link": "https://i.postimg.cc/W4nM5tBk/seleccionar-todo-1.png"},
                {"pantalla": "2","opcion":"LIMPIEZA", "link": "https://i.postimg.cc/vHrWxFgS/productos.png"},
                {"pantalla":"3","opcion": "INSUMOS", "link": "https://i.postimg.cc/qBcLyTyC/comida-1.png"},
                {"pantalla":"4","opcion": "DESECHABLES", "link": "https://i.postimg.cc/qq2s49Hn/contenedor-de-comida.png"},
                {"pantalla":"5","opcion": "LOZA", "link": "https://i.postimg.cc/tg6nZJ56/vajilla.png"},

            ]
        }
        
    elif categoria=="empleados":
        context = {
            "opciones": [
                {"pantalla":"6","opcion": "MOSTRAR TODO", "link": "https://i.postimg.cc/W4nM5tBk/seleccionar-todo-1.png"},
                {"pantalla":"7","opcion": "COCINA", "link": "https://i.postimg.cc/6QnJcnb6/camarero.png"},
                {"pantalla":"8","opcion": "MESERO", "link": "link3"},
                {"pantalla":"9","opcion": "RH", "link": "link4"},
                {"pantalla":"10","opcion": "RECEPCIONISTA", "link": "link5"},

            ]
        }
        
    return render(request, 'productos_app/submenus.html', context)

@login_required
def tablas(request, subcategoria):
    context = {}
    if subcategoria=="1":
        context = {
            "titulo":"Mostrar todo"
        }
    elif subcategoria=="2":
        context = {
            "titulo":"Limpieza"
        }
    elif subcategoria=="3":
        context = {
            "titulo":"Insumos"
        }
    elif subcategoria=="4":
        context = {
            "titulo":"Desechables"
        }
    elif subcategoria=="5":
        context = {
            "titulo":"Loza"
        }
    elif subcategoria=="6":
        context = {
            "titulo":"Mostrar todo"
        }
    elif subcategoria=="7":
        context = {
            "titulo":"Cocina"
        }
    elif subcategoria=="8":
        context = {
            "titulo":"Mesero"
        }
    elif subcategoria=="9":
        context = {
            "titulo":"RH"
        }
    elif subcategoria=="10":
        context = {
            "titulo":"Recepcionista"
        }

    return render(request, 'productos_app/tablas.html', context)


@login_required
def proveedores(request):
    pass
