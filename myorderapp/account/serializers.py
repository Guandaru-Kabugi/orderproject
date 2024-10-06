from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)
    class Meta:
        model =User
        fields = ['id','token','username','email','first_name','last_name']
    # def validate_username(self, value):
        
    #     if User.objects.filter(username=value).exists():
    #         raise serializers.ValidationError("username already exists")
    #     return value