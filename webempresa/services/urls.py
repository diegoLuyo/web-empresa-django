from django.urls import path
from . import views as views_services
urlpatterns = [
    path('', views_services.servicios, name="servicios"),


]
