from django.db import models
from django.contrib.auth.models import User

class Comentarios(models.Model):
    articulo = models.ForeignKey('articulos.Articulo', on_delete=models.CASCADE, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)


def __str__(self):
    if self.articulo:
        return f'Comentario de {self.usuario.username} en {self.articulo.titulo}'
    else:
        return f'Comentario de {self.usuario.username}'
