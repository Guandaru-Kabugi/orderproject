from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Order
from rest_framework.generics import ListAPIView
from .serializers import OrderSerializer
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .filters import OrderFilter
# Create your views here.
@authentication_classes([TokenAuthentication,SessionAuthentication,BasicAuthentication])
@permission_classes([IsAuthenticated])
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

