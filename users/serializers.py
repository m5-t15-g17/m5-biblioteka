from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'books', 'username', 'email', 'is_auth', 'is_admin', 'password']
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {
                'validators': [UniqueValidator(queryset = User.objects.all(), message = 'Username already in use.')]
            },
            'email': {
                'validators': [UniqueValidator(queryset = User.objects.all(), message = 'Email already registered.')]
            },
            'password': {'write_only': True},
            'books': {'read_only': True},
        }

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)
        return user
    
    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
            if key == 'password':
                instance.set_password(value)
                
        instance.save()
        return instance
    
