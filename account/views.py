from django.shortcuts import render
from account.serializers import BalanceSerializer, PlanSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Balance, Plans

# Create your views here.
@api_view(['GET'])
def balance(request):
  bal_objs=Balance.objects.latest('balance')
  serializer=BalanceSerializer(bal_objs)
  return Response({'status':200,'payload':serializer.data})

@api_view(['GET'])
def plan(request):
  plan_objs=Plans.objects.latest('plan')
  serializer=PlanSerializer(plan_objs)
  return Response({'status':200,'payload':serializer.data})

