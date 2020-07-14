from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request,"blog/blog.html", {"posts": posts})

def categoria(request, id_categoria):
    categoria=get_object_or_404(Category,id=id_categoria)
    return render(request, "blog/categoria.html", {"categoria":categoria})