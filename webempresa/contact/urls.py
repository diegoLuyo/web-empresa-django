from django.urls import path
from . import views as views_contact
urlpatterns = [
    path('', views_contact.contacto, name="contacto"),


]

