from django.urls import path
from . import views as views_page
urlpatterns = [
    path('<int:page_id>/<slug:page_slug>', views_page.page, name="page"),
   
]

