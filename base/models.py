from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    id = models.BigAutoField(primary_key=True)
    desc = models.CharField(max_length=20)
    price = models.FloatField()


    def __str__(self):
        return self.desc