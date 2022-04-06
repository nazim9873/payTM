from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ticketBooking.serializers import FlightSerializer
from .models import Balance, Flights, Plans


@api_view(['GET'])
def flight(request):
  flight_objs=Flights.objects.latest('plan')
  serializer=FlightSerializer(flight_objs)
  return Response({'status':200,'payload':serializer.data})

@api_view(['POST'])
def post_flight(request):
  data=request.data
  serializer=FlightSerializer(data=data)
  if not serializer.is_valid():
    return Response({'status':403,'errors':serializer.errors,'message':'Something went wrong'})
  serializer.save()
  print(data)
  return Response({'status':200,'payload':serializer.data,'message':data['message']})

@api_view(['PUT'])
def update_flight(request,id):
  try:
    flight_obj=Flights.objects.get(id=id)
    serializer=FlightSerializer(flight_obj,data=request.data,partial=True)
    if not serializer.is_valid():
     return Response({'status':403,'errors':serializer.errors,'message':'Something went wrong'})
    serializer.save()
    return Response({'status':200,'payload':serializer.data,'message':"Updated"})
  except Exception as e:
    return Response({'status':403,'message':'invalid'})

@api_view(['DELETE'])
def delete_flight(request,id):
  try:
    flight_obj=Flights.objects.get(id=id)
    flight_obj.delete()
    return Response({'status':200,'message':"Deleted"})
  except Exception as e:
      return Response({'status':403,'message':'invalid'})


# Create your views here.
