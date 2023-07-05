from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Loan
from .serializers import LoanSerializer
from copies.models import Copy
from users.models import User

class LoanView(generics.CreateAPIView):
    

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_url_kwarg = "copy_id"

    def get_queryset(self):
        queryset = super().get_queryset()
        instance_trait = get_object_or_404(User, pk=self.kwargs.get("user_id"))

        return queryset.filter(users=instance_trait)
    

    def perform_create(self, serializer):
        instance_copy = get_object_or_404(Copy, pk=self.kwargs.get("copy_id"))
        instance_user = get_object_or_404(User, pk=self.kwargs.get("user_id")) 

        return serializer.save(user_id = instance_user, copy_id = instance_copy)
    
    # def perform_create(self, serializer):
    #     return serializer.save(user_id=self.request.query_params.get())



