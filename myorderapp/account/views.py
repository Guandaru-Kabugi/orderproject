from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import response,status
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.authtoken.models import Token
# Create your views here.
@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = get_object_or_404(User,email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return response.Response({"token":token.key,"user":serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return response.Response({"error":"invalid data format"}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def login(request):
    user = get_object_or_404(User,username=request.data['username'])
    if user:
        if not user.check_password(request.data['password']):
            return response.Response({"Error":"Invalid Details"},status=status.HTTP_400_BAD_REQUEST)
        token,created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        return response.Response({"token":token.key, "user":serializer.data}, status=status.HTTP_200_OK)
    
        