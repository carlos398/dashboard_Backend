from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import UserProfile

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "email", "name", "last_name", "is_active","is_staff", "last_login", "password"]

    
    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user