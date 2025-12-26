# Create your views here.
from django.shortcuts import render
from .models import Universitet, Direktor

def universitet_list(request):
    universitetlar = Universitet.objects.all()
    return render(request, "universitet_list.html", {"universitetlar": universitetlar})

def direktor_list(request):
    direktorlar = Direktor.objects.all()
    return render(request, "direktor_list.html", {"direktorlar": direktorlar})
