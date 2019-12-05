#from django.contrib import admin
from django.urls import path
from .views import home, solicitar, modelos, listar, eliminar, modificar
#from django.contrib.auth.views import LoginView
from django.urls import path, include

urlpatterns = [
    path('', home, name="home"),
    #path('', login, LoginView.as_view(template_name='login.html'), name="login"),
    path('home/', home, name="home"),
    path('solicitar/',solicitar, name="solicitar"),
    path('modelos/',modelos, name="modelos"),
    path('listar/',listar, name="listar"),
    path('eliminar/<id>/',eliminar, name="eliminar"),
    path('modificar/<id>/',modificar, name="modificar"),
    path('accounts/', include('django.contrib.auth.urls')),
    ]
#Add Django site authentication urls (for login, logout, password management)
#urlpatterns += [
 #   path('accounts/', include('django.contrib.auth.urls')),
#]