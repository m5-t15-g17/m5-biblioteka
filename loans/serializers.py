from rest_framework import serializers
from .models import Loan

class LoarnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [None]