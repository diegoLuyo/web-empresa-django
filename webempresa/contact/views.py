from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.
def contacto(request):
    contact_form=ContactForm()

    if request.method== "POST":
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            nombre=request.POST.get('name', '')
            email=request.POST.get('email', '')
            contenido=request.POST.get('contenido', '')
            #Enviamos el correo y redireccionamos
            email_respuesta=EmailMessage(
                "La Cafetiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\n Escribio: \n\n{}".format(nombre,email,contenido),
                "no-contestar@inbox.mailtrap.io",
                ["diegoluyoquispe@gmail.com"],
                reply_to=[email]
            )
            try:
                email_respuesta.send()
                #todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contacto')+"?ok")
            except:
                #algo no ha ido bien redireccionamos a fail
                return redirect(reverse('contacto')+"fail")
    return render(request,"contact/contact.html", {'form':contact_form})