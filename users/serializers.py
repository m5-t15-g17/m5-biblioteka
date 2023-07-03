from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields = ['id', 'books', 'username', 'email', 'is_auth', 'is_admin', 'book_history', 'password']
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {
                'validators': [UniqueValidator(queryset = User.objects.all(), message = 'Username already in use.')]
            },
            'email': {
                'validators': [UniqueValidator(queryset = User.objects.all(), message = 'Email already registered.')]
            },
            'password': {'write_only': True}
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create(**validated_data)