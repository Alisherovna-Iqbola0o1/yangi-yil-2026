# Create your views here.

from django.shortcuts import render
from .models import Maktab, Direktor, Oqituvchi

def maktab_list(request):
    maktablar = Maktab.objects.all()
    return render(request, "maktab_list.html", {"maktablar": maktablar})

def direktor_list(request):
    direktorlar = Direktor.objects.all()
    return render(request, "direktor_list.html", {"direktorlar": direktorlar})

def oqituvchi_list(request):
    oqituvchilar = Oqituvchi.objects.all()
    return render(request, "oqituvchi_list.html", {"oqituvchilar": oqituvchilar})
