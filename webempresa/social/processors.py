from .models import Link

def ctx_dict(request):
    ctx = {}
    links =Link.objects.all()
    for enlace in links:
        ctx[enlace.clave] = enlace.url
    return ctx