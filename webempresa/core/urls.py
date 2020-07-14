from django.urls import path
from . import views as views_core
urlpatterns = [
    path('', views_core.home,name="home"),
    path('about/', views_core.about ,name="about"),
    path('tienda/', views_core.tienda, name="tienda"),
    


]

