from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirmed_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'confirmed_password', 'city', 'state', 'address', 'phone']

    def validate(self, data):
        if data['password'] != data['confirmed_password']:
            raise serializers.ValidationError('Passwords do not match.')
        return data
    
    def create(self, validated_data):
        validated_data.pop('confirmed_password', None)
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.password = make_password(password)
        user.save()
        return user