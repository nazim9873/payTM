from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Balance(models.Model):
  user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  balance=models.IntegerField(null=True)

  def __str__(self):
    return self.user

class Plans(models.Model):
  user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
  plan=models.CharField(max_length=200,null=True)

  def __str__(self):
    return self.user