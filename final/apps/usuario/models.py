from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    imagen = models.ImageField(null=True, blank=True, upload_to='usuario', default='usuario/usuario_defecto.jpg')

    def get_absolute_url(self):
        return reverse('index')
# Create your models here.
