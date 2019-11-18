from django.shortcuts import render, redirect
from .models import Persona
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'renta/home.html')

def solicitar(request):

    personas= Persona.objects.all()
    variables = {
        'personas':personas
    }

    if request.POST:
        persona = Persona()
        persona.nombre = request.POST.get('nombre')
        persona.apellido = request.POST.get('apellido')
        persona.run = request.POST.get('run')
        persona.correo = request.POST.get('correo')

        try:
            persona.save()
            variables['mensaje'] = 'Guardado Exitoso'
        
        except:
            variables['mensaje'] = 'No se ha guardado'


    return render(request, 'renta/solicitar.html', variables)

def modelos(request):
    return render(request, 'renta/modelos.html')

    #CRUD
def listar(request):

    personas = Persona.objects.all()

    return render(request, 'renta/listar.html', {'personas':personas})

def eliminar (request, id):
    persona = Persona.objects.get(id=id)
    try:
        persona.delete()
        mensaje = "Eliminado Correctamente"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha eliminado"
        messages.error(request, mensaje)

    return redirect("listar")

def modificar(request, id):
    persona = Persona.objects.get(id=id)
    variables = {
        'persona':persona
    }

    if request.POST:
        persona = Persona()
        persona.id= request.POST.get('id')
        persona.nombre = request.POST.get('nombre')
        persona.apellido = request.POST.get('apellido')
        persona.run = request.POST.get('run')
        persona.correo = request.POST.get('correo')

        try:
            persona.save()
            messages.success(request, 'Datos modificados ')
        
        except:
            messages.error(request, 'No se ha podido modificar ')

        return redirect('listar')

    return render(request, 'renta/modificar.html',variables)