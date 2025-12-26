from django.db import models
from django import User

# Create your models here.

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
