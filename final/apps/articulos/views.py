from django.shortcuts import render, get_object_or_404
from .models import Articulo
from django.views.generic import ListView
from apps.comentarios.models import Comentarios


def ArticuloView(request):
   articulos = Articulo.objects.all()
   return render(request, 'articulos.html', {'articulos': articulos})

def ArticuloDetailView(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    comentarios = Comentarios.objects.filter(articulo=articulo)
    return render(request, 'articulo_detalle.html', {
        'articulo': articulo,
        'comentarios': comentarios
    })

# class ArticuloListView(ListView):
#     model = Articulo
#     template_name = 'articulos.html'
#     context_object_name = 'articulos'

# Create your views here.
