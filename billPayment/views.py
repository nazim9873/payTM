from django.shortcuts import render
from billPayment.serializers import MobileRechargeSerializer, PayRentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *


@api_view(['GET'])
def recharge(request):
  recharge_objs=MobileRecharge.objects.latest('plan')
  serializer=MobileRechargeSerializer(recharge_objs)
  return Response({'status':200,'payload':serializer.data})

@api_view(['POST'])
def post_recharge(request):
  data=request.data
  serializer=MobileRechargeSerializer(data=data)
  if not serializer.is_valid():
    return Response({'status':403,'errors':serializer.errors,'message':'Something went wrong'})
  serializer.save()
  print(data)
  return Response({'status':200,'payload':serializer.data,'message':data['message']})

@api_view(['GET'])
def payrent(request):
  payrent_objs=PayRent.objects.latest('plan')
  serializer=PayRentSerializer(payrent_objs)
  return Response({'status':200,'payload':serializer.data})

@api_view(['POST'])
def post_payrent(request):
  data=request.data
  serializer=PayRentSerializer(data=data)
  if not serializer.is_valid():
    return Response({'status':403,'errors':serializer.errors,'message':'Something went wrong'})
  serializer.save()
  print(data)
  return Response({'status':200,'payload':serializer.data,'message':data['message']})
