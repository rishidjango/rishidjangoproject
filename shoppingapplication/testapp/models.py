from django.db import models
from django.contrib.auth.models import User
class goods(models.Model):
    gname=models.CharField(max_length=40)
    gprice=models.IntegerField()
    gquantity=models.IntegerField()
    gseller=models.CharField(max_length=40)
    gming=models.FileField(blank=True)
class cart(models.Model):
    user_id=models.ForeignKey(User,related_name="cartitems",on_delete=models.CASCADE)
    gname=models.CharField(max_length=50)
    gprice=models.IntegerField()
    gquantity=models.IntegerField()
