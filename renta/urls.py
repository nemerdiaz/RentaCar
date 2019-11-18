from django.urls import path
from .views import home , solicitar, modelos, listar, eliminar, modificar

urlpatterns = [
    path('', home, name="home"),
    path('solicitar/',solicitar, name="solicitar"),
    path('modelos/',modelos, name="modelos"),
    path('listar/',listar, name="listar"),
    path('eliminar/<id>/',eliminar, name="eliminar"),
    path('modificar/<id>/',modificar, name="modificar"),
    ]