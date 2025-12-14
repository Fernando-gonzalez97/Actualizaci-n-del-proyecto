from django.urls import path
from .views import ArticuloView, ArticuloDetailView

urlpatterns = [
    path('articulos/', ArticuloView, name='articulos'),
    path('articulos/<int:pk>/', ArticuloDetailView, name='articulo_detalle'),
]