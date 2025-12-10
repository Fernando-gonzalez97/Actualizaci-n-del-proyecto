from django.urls import path
from .views import ArticuloView

urlpatterns = [
    path('articulos/', ArticuloView, name='articulos'),

]