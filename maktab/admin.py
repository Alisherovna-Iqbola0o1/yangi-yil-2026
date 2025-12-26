from django.contrib import admin
from .models import Maktab, Direktor
# Register your models here.

@admin.register(Maktab)
class MaktabAdmin(admin.ModelAdmin):
    list_display = ("name", "manzil", "oquvchilar_soni", "maktab_ochilgan_vaqt", "created_at")
    search_fields = ("name", "manzil")

@admin.register(Direktor)
class DirektorAdmin(admin.ModelAdmin):
    list_display = ("user", "oylik", "ishga_kelgan_vaqt", "created_at")
    search_fields = ("user__username",)
