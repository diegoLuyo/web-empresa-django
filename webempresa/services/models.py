from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo= models.CharField(max_length=200)
    subtitulo= models.CharField(max_length=200)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to="services")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update= models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    class meta:
        verbose_name="servicio"
        verbose_name_plural="servicios"
        ordering=['-created']

    def __str__(self):
        return self.titulo
     
