from rest_framework import serializers
from .models import Copy


class CopySerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Copy.objects.create(**validated_data)

    class Meta:
        model = Copy
        fields = ["id", "copyNumber", "book"]
