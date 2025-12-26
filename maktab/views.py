# Create your views here.

from django.shortcuts import render
from .models import Maktab, Direktor

def maktab_list(request):
    maktablar = Maktab.objects.all()
    return render(request, "maktab_list.html", {"maktablar": maktablar})

def direktor_list(request):
    direktorlar = Direktor.objects.all()
    return render(request, "direktor_list.html", {"direktorlar": direktorlar})
