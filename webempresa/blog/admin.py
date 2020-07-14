from django.contrib import admin
from .models import Category, Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')
    list_display=('titulo', 'autor','published','post_categories')
    ordering=('autor','published')
    search_fields = ('titulo','contenido','autor__username')
    list_filter=('autor__username','categorias__nombre')

    def post_categories(self, obj):
        return ", ".join([c.nombre for c in  obj.categorias.all().order_by("nombre")])

    post_categories.short_description="Categorias"

#registrar los cambios en el administrador

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)