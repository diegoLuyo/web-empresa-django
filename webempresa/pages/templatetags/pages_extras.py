from django import template
from pages.models import Pages

register = template.Library()

""" un decorador que va implementar una nueva funcionalidad """
@register.simple_tag

def get_page_list():
    pages = Pages.objects.all()
    return pages