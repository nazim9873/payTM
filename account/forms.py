from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from account.models import Balance


class CreateUserForm(UserCreationForm):
  class Meta:
    model=User
    fields=['username','email','password1','password2']

class BalanceForm(ModelForm):
  class Meta:
    model=Balance
    fields="__all__"