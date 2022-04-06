from rest_framework import serializers
from .models import Flights,Train,Bus

class MobileRechargeSerializer(serializers.ModelSerializer):
  class Meta:
    model=Flights
    fields='__all__'

  def validate(self,data):
    if data['travellors']<=0:
        raise serializers.ValidationError({'error':'Must be greater than 0'})
    return data

class PayRentSerializer(serializers.ModelSerializer):
  class Meta:
    model=Train
    fields='__all__'

class RechargeDTHSerializer(serializers.ModelSerializer):
  class Meta:
    model=Bus
    fields='__all__'