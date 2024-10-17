from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def menu_principal(request):
    return render(request, 'productos_app/menu_principal.html')

@login_required
def submenus(request, nombre):
    context = {}

    if nombre == "productos":
        context = {
            "opciones": [
                {"pantalla":"1","opcion": "MOSTRAR TODO", "link": "https://i.postimg.cc/W4nM5tBk/seleccionar-todo-1.png"},
                {"pantalla":"2","opcion":"LIMPIEZA", "link": "https://i.postimg.cc/vHrWxFgS/productos.png"},
                {"pantalla":"3","opcion": "INSUMOS", "link": "https://i.postimg.cc/qBcLyTyC/comida-1.png"},
                {"pantalla":"4","opcion": "DESECHABLES", "link": "https://i.postimg.cc/qq2s49Hn/contenedor-de-comida.png"},
                {"pantalla":"5","opcion": "LOZA", "link": "https://i.postimg.cc/tg6nZJ56/vajilla.png"},

            ]
        }
        
    elif nombre=="empleados":
        context = {
            "opciones": [
                {"pantalla":"6","opcion": "MOSTRAR TODO", "link": "https://i.postimg.cc/W4nM5tBk/seleccionar-todo-1.png"},
                {"pantalla":"7","opcion": "COCINA", "link": "https://i.postimg.cc/bwKtLkVr/chef-masculino.png"},
                {"pantalla":"8","opcion": "MESERO", "link": "https://i.postimg.cc/6QnJcnb6/camarero.png"},
                {"pantalla":"9","opcion": "RH", "link": "https://i.postimg.cc/LsnBFVFR/gerente-de-recursos-humanos.png"},
                {"pantalla":"10","opcion": "RECEPCIONISTA", "link": "https://i.postimg.cc/LX4SshvH/recepcionista.png"},

            ]
        }
        
    return render(request, 'productos_app/submenus.html', context)

@login_required
def tablas(request, nombre):
    context = {}
    if nombre=="1":
        context = {
            "titulo":"Mostrar todo"
        }
    elif nombre=="2":
        context = {
            "titulo":"Limpieza"
        }
    elif nombre=="3":
        context = {
            "titulo":"Insumos"
        }
    elif nombre=="4":
        context = {
            "titulo":"Desechables"
        }
    elif nombre=="5":
        context = {
            "titulo":"Loza"
        }
    elif nombre=="6":
        context = {
            "titulo":"Mostrar todo"
        }
    elif nombre=="7":
        context = {
            "titulo":"Cocina"
        }
    elif nombre=="8":
        context = {
            "titulo":"Mesero"
        }
    elif nombre=="9":
        context = {
            "titulo":"RH"
        }
    elif nombre=="10":
        context = {
            "titulo":"Recepcionista"
        }

    return render(request, 'productos_app/tablita.html', context)


@login_required
def proveedores(request):
    pass
