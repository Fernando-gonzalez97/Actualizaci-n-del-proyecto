from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Comentarios
from apps.articulos.models import Articulo


def ComentariosView(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        articulo_id = request.POST.get('articulo_id')
        
        if request.user.is_authenticated and contenido and articulo_id:
            articulo = get_object_or_404(Articulo, pk=articulo_id)
            Comentarios.objects.create(usuario=request.user, contenido=contenido, articulo=articulo)
            messages.success(request, 'Comentario agregado exitosamente.')
            return redirect('articulo_detalle', pk=articulo_id)
    
    comentarios = Comentarios.objects.all()
    return render(request, 'comentarios.html', {'comentarios': comentarios})

@login_required  
def eliminar_comentario(request, pk): 
    comentario = get_object_or_404(Comentarios, pk=pk)
    articulo_id = comentario.articulo.pk
    
    if comentario.usuario == request.user or request.user.is_staff:
        if request.method == 'POST':
            comentario.delete()
            messages.success(request, 'Comentario eliminado exitosamente.')
            return redirect('articulo_detalle', pk=articulo_id)
    else:
        messages.error(request, 'No tienes permiso para eliminar este comentario.')
        return redirect('articulo_detalle', pk=articulo_id)
    
    return render(request, 'comentarios_eliminar.html', {'comentario': comentario})  

@login_required
def editar_comentario(request, pk):
    comentario = get_object_or_404(Comentarios, pk=pk)
    articulo_id = comentario.articulo.pk
    
    if comentario.usuario != request.user:
        messages.error(request, 'No tienes permiso para editar este comentario.')
        return redirect('articulo_detalle', pk=articulo_id)
    
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if contenido:
            comentario.contenido = contenido
            comentario.save()
            messages.success(request, 'Comentario actualizado exitosamente.')
            return redirect('articulo_detalle', pk=articulo_id)
    
    return render(request, 'comentarios_editar.html', {'comentario': comentario})