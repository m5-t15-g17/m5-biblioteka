from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        book = Book
        fields = ["id", "user", "copy_id", "description", "is_available", "name"]
        extra_kwargs = {"copy_id": {"read_only": True}}

    def create(self, validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)

    def update(self, validated_data: dict, instance: Book) -> Book:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance

    def delete():
        return
