from django.shortcuts import render

# Create your views here.

def A(request):
     return render(request, "Universitet.html")

def B(request):
     return render(request, "Direktor.html")