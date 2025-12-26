from django.contrib import admin
from .models import Universitet, Direktor
# Register your models here.

from django.contrib import admin
from .models import Universitet, Direktor

@admin.register(Universitet)
class UniversitetAdmin(admin.ModelAdmin):
    list_display = ("name", "manzil", "oquvchilar_soni", "created_at")
    search_fields = ("name", "manzil")  

@admin.register(Direktor)
class DirektorAdmin(admin.ModelAdmin):
    list_display = ("oylik", "ishga_kelgan_vaqti", "yaratilgan_vaqti")
    search_fields = ("oylik",) 
