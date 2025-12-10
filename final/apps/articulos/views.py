from django.shortcuts import render
from .models import Articulo
from django.views.generic import ListView


def ArticuloView(request):
   articulos = Articulo.objects.all()
   return render(request, 'articulos.html', {'articulos': articulos})

# class ArticuloListView(ListView):
#     model = Articulo
#     template_name = 'articulos.html'
#     context_object_name = 'articulos'

# Create your views here.
