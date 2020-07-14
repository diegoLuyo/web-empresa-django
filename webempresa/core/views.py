from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"core/index.html")

def about(request):
    return render(request,"core/about.html")

def tienda(request):
    return render(request,"core/store.html")



