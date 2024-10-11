from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='productos_app/login.html'), name='login'),
    path('menu_principal/', views.menu_principal, name='menu_principal'),
    path('<str:categoria>/', views.submenus, name="submenus"),
    path('proveedores/', views.proveedores, name='proveedores'),
]

