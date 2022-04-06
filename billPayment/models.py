from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MobileRecharge(models.Model):
  user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  number=models.IntegerField()

  def __str__(self):
    return self.number

class PayRent(models.Model):
  user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  mode=models.CharField(max_length=100)
  recepient_id=models.IntegerField()

  def __str__(self):
    return self.recepient_id

class RechargeDTH(models.Model):
  user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  dth_operator=models.CharField(max_length=100)
  customer_id=models.IntegerField()

  def __str__(self):
    return self.customer_id