from django.contrib import admin
from .models import Maktab, Direktor, Oqituvchi
# Register your models here.

@admin.register(Maktab)
class MaktabAdmin(admin.ModelAdmin):
    list_display = ("name", "manzil", "oquvchilar_soni", "maktab_ochilgan_vaqt", "created_at")
    search_fields = ("name", "manzil")

@admin.register(Direktor)
class DirektorAdmin(admin.ModelAdmin):
    list_display = ("user", "oylik", "ishga_kelgan_vaqt", "created_at")
    search_fields = ("user__username",)

@admin.register(Oqituvchi)
class OqituvchiAdmin(admin.ModelAdmin):
    list_display = ("user", "yosh", "oylik_maosh", "ishga_kirgan_vaqti", "oquvchilar_soni", "yaratilgan_vaqti", "ozgartirilgan_vaqti")
    search_fields = ("user__username",)