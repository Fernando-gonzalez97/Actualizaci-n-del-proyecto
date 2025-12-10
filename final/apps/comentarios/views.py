from django.shortcuts import render, redirect
from .models import Comentarios

def ComentariosView(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if request.user.is_authenticated and contenido:
            Comentarios.objects.create(usuario=request.user, contenido=contenido)
            return redirect('comentarios')
    
    comentarios = Comentarios.objects.all()
    return render(request, 'comentarios.html', {'comentarios': comentarios})