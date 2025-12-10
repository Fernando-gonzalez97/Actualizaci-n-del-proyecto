from django.contrib import admin
from .models import Comentarios

@admin.register(Comentarios)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'contenido', 'fecha_creacion'] 
    list_filter = ['fecha_creacion']
    search_fields = ['usuario__username', 'contenido']