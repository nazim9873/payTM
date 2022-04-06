from rest_framework import serializers
from .models import Flights,Train,Bus

class FlightSerializer(serializers.ModelSerializer):
  class Meta:
    model=Flights
    fields='__all__'

  def validate(self,data):
    if data['travellors']<=0:
        raise serializers.ValidationError({'error':'Must be greater than 0'})
    return data

class TrainSerializer(serializers.ModelSerializer):
  class Meta:
    model=Train
    fields='__all__'

class BusSerializer(serializers.ModelSerializer):
  class Meta:
    model=Bus
    fields='__all__'