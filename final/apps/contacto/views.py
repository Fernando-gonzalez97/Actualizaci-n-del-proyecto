from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contacto


def ContactoView(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        Contacto.objects.create(nombre=nombre, email=email, mensaje=mensaje)
        messages.success(request, '¡Felicitaciones! Tu mensaje ha sido enviado')
        return redirect('contacto')
    
    contactos = Contacto.objects.all()
    return render(request, 'contacto.html', {'contactos': contactos})