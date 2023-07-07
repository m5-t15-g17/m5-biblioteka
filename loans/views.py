from django.shortcuts import get_object_or_404
from rest_framework import generics

from users.serializers import UserSerializer
from .models import Loan
from .serializers import LoanSerializer
from users.models import User
from datetime import datetime
from rest_framework.views import Request, Response, status

class LoanView(generics.CreateAPIView):
    
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_url_kwarg = "copy_id"

    def get_queryset(self):
        queryset = super().get_queryset()
        instance_trait = get_object_or_404(User, pk=self.kwargs.get("user_id"))

        return queryset.filter(users=instance_trait)
    
    def post(self, request):
        user = get_object_or_404(User, id = self.request.user.id)

        if user.is_blocked:
             return Response({'error': 'User blocked'})
        
        loans = user.loan.all()

        # falta a lógica de criação aqui no meio e depois vem a parte novamente de verificação se o usuário tem em mãos um livro em atraso.
        
        for loan in loans:
            if loan.return_date < datetime.now():
                serializer = UserSerializer(user, {'is_blocked': True}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return Response({'error': 'User blocked'})
    
    def patch(self, request: Request):
        user = get_object_or_404(User, id = self.request.user.id)

        self.check_object_permissions(request, user)
        loans = user.loan.all()

        for loan in loans:
            if loan.return_date < datetime.now():
                serializer = UserSerializer(user, {'is_blocked': True}, partial = True)
                serializer.is_valid(raise_exception = True)
                serializer.save()

                break
                        
        loan = get_object_or_404(Loan, id=self.kwargs.get('loan_id'))

        setattr(loan, 'return_date', datetime.now)

        loan.save()

        serializer = LoanSerializer(loan)
    
        return Response(serializer.data, 200)



