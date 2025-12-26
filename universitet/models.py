from django.db import models
from django import User

# Create your models here.
# 2: Universitet class  name, manzil, oquvchilar soni, maktab-ochilgan-vaqt, yaratilgan vaqt  Direktor class 
# forinkey user, oylik, ishga-kelgan-vaqt, yaratilgan vaqt

class Universitet(models.Model):
    name = models.CharField(max_length=255)
    manzil = models.CharField(max_length=100)
    oquvchilar_soni = models.IntegerField()
    created_at = models.DateField()

    def __str__(self):
        return self.name
