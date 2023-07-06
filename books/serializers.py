from rest_framework import serializers

from books.models import Book
from users.serializers import UserSerializer


class BookSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    def create(self, validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)

    class Meta:
        model = Book
        fields = ["id", "user", "description", "is_available", "name"]

    def update(self, instance: Book, validated_data: dict) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def delete():
        return
