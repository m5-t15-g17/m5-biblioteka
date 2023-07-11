from django.shortcuts import get_object_or_404
from rest_framework import generics
from books.serializers import BookSerializer

from users.serializers import UserSerializer
from .models import Loan
from .serializers import LoanSerializer
from copies.serializers import CopySerializer
from books.serializers import BookSerializer
from books.models import Book
from copies.models import Copy
from users.models import User
from datetime import datetime
from rest_framework.views import Request, Response, status

class LoanView(generics.CreateAPIView):
    
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        instance_user = get_object_or_404(User, pk=self.request.user.id)

        return queryset.filter(users=instance_user)
    
    # def post(self, request):
    #     user = get_object_or_404(User, id = self.request.user.id)

    #     if user.is_blocked:
    #          return Response({'error': 'User blocked'})
        
    #     loans = user.loan.all()

    #     # falta a lógica de criação aqui no meio e depois vem a parte novamente de verificação se o usuário tem em mãos um livro em atraso.
        
    #     for loan in loans:
    #         if loan.return_date < datetime.now():
    #             serializer = UserSerializer(user, {'is_blocked': True}, partial=True)
    #             serializer.is_valid(raise_exception=True)
    #             serializer.save()

    #             return Response({'error': 'User blocked'})
            
    def perform_create(self, serializer):

        # print(self.request.user)

        user = get_object_or_404(User, pk=self.request.user.id)
        copy = get_object_or_404(Copy, pk=self.kwargs.get("pk"))
        copys = copy.book
        print(user)
        print('oi', copy)
        print('olá', copys)

        for copy in copys:
            if copy.id == self.kwargs.get("pk"):
                if(copy.copyNumber == 0):

                    book = get_object_or_404(Book, pk=copy.book)
                    serializer = BookSerializer(book,{"is_avaliable":False}, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    return Response("no copies left", 400)

                serializer = CopySerializer(copy,{'copyNumber':"copyNumber"-1}, partial=True )
                serializer.is_valid(raise_exception=True)
                serializer.save()
            else:
                serializer = BookSerializer(book, {'is_avaliable': False}, partial = True)

        serializer.save(copy = copy, user = user)
        
        print(serializer)

        return Response(serializer.validated_data)
    
    def patch(self, request: Request):
        user = get_object_or_404(User, id = self.request.user.id)

        self.check_object_permissions(request, user)
        loans = user.loan.all()
        copy = get_object_or_404(Copy, pk=self.kwargs.get("pk"))
        copys = copy.loan.all()

        for copy in copys:
            if copy.id == self.kwargs.get("pk"):
                if(copy.copyNumber == 0):

                    book = get_object_or_404(Book, pk=copy.book)
                    serializer = BookSerializer(book,{"is_avaliable":True}, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    
                serializer = CopySerializer(copy,{'copyNumber':"copyNumber"+1}, partial=True )
                serializer.is_valid(raise_exception=True)
                serializer.save()

                break

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



