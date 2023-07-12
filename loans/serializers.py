from rest_framework import serializers
from .models import Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ["id", "user", "copy", "return_date", "loan_date", "expected_return"]
        read_only_fields = ["user", "copy", "return_date", "loan_date", "expected_return"]

    def create(self, validated_data):
        return Loan.objects.create(**validated_data)