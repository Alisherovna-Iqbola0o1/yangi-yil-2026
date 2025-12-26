from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Maktab(models.Model):
    name = models.CharField(max_length=50)
    manzil = models.CharField(max_length=255)
    oquvchilar_soni = models.PositiveIntegerField()
    maktab_ochilgan_vaqt = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Direktor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    oylik = models.DecimalField()
    ishga_kelgan_vaqt = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.user



