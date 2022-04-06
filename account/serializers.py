from rest_framework import serializers
from .models import Balance,Plans

class BalanceSerializer(serializers.ModelSerializer):
  class Meta:
    model=Balance
    fields='__all__'

  def validate(self,data):
    if not data['balance'].isnumeric():
        raise serializers.ValidationError({'error':'Balance cant be character!!'})
    return data

class PlanSerializer(serializers.ModelSerializer):
  class Meta:
    model=Plans
    fields='__all__'
