from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Flights(models.Model):
  user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  fromwhere=models.CharField(max_length=100)
  towhere=models.CharField(max_length=100)
  departure_date=models.DateField(default=date.today())
  travellors=models.IntegerField()
  travellor_class=models.CharField(max_length=100)

class Bus(models.Model):
  user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  fromwhere=models.CharField(max_length=100)
  towhere=models.CharField(max_length=100)
  departure_date=models.DateField(default=date.today())

class Train(models.Model):
  user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  fromstation=models.CharField(max_length=100)
  tostation=models.CharField(max_length=100)
  departure_date=models.DateField(default=date.today())



