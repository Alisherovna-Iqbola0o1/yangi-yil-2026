from django.db import models
from django import User

# Create your models here.
# 2: Universitet class  name, manzil, oquvchilar soni, maktab-ochilgan-vaqt, yaratilgan vaqt  Direktor class 
# forinkey user, oylik, ishga-kelgan-vaqt, yaratilgan vaqt
# 2: universitet va direktor nomli classlarni yaratib bo'lib makemigrations va migrate qiling. 
# admin.py faylga ham qoshing va admin panelga kirib bittadan malumot qoshing.

class Universitet(models.Model):
    name = models.CharField(max_length=255)
    manzil = models.CharField(max_length=100)
    oquvchilar_soni = models.CharField(max_length=100)
    created_at = models.DateField()

    def __str__(self):
        return self.name

class Direktor(models.Model):
    oylik = models.IntegerField()
    ishga_kelgan_vaqti = models.DateField()
    yaratilgan_vaqti = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Direktor {self.id}"
