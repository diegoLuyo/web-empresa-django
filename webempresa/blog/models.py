from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    nombre= models.CharField(max_length=100)
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update= models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    class Meta():
        verbose_name="categoria"
        verbose_name_plural="categorias"
        ordering=['-created']

    def __str__(self):
        return self.nombre
class Post(models.Model):
    titulo= models.CharField(max_length=200)
    contenido= models.TextField()
    published= models.DateField(verbose_name="Fecha de publicacion", default=now)
    imagen= models.ImageField(upload_to="blog", null=True,blank=True)
    autor=models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update= models.DateTimeField(auto_now=True, verbose_name="Fecha de Edicion")

    class Meta():
        verbose_name="entrada"
        verbose_name_plural="entradas"
        ordering=['-created']

    def __str__(self):
        return self.titulo

