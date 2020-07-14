from django.urls import path
from . import views as views_blog
urlpatterns = [
    path('', views_blog.blog, name="blog"),
    path('categoria/<int:id_categoria>/', views_blog.categoria, name="categoria"),
   
]

