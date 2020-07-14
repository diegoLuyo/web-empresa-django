from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Pages(models.Model):
    titulo=models.CharField(verbose_name="Título", max_length=200)
    contenido=RichTextField(verbose_name="Contenido")
    order =models.SmallIntegerField(verbose_name="Orden", default=0)
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "páginas"
        verbose_name_plural="páginas"
        ordering=['order', 'titulo']

    def __str__(self):
        return self.titulo
     