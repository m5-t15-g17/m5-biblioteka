from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import request
from users.serializers import UserSerializer
from .models import Loan
from .serializers import LoanSerializer
from copies.serializers import CopySerializer
from books.serializers import BookSerializer
from books.models import Book
from copies.models import Copy
from users.models import User
from datetime import date
from rest_framework.views import Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import pdb
from datetime import timedelta
from django.forms import model_to_dict
from rest_framework import serializers


class LoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "pk"

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        instance_user = get_object_or_404(User, id=self.request.user.id)

        return queryset.filter(users=instance_user)

    def perform_create(self, serializer):
        returnDate = date.today()
        returnDate = returnDate + timedelta(7, 0)

        user = self.request.user
        if user.is_block:
            raise serializers.ValidationError("User blocked")
        loans = user.loans.all()

        for loan in loans:
            if loan.expected_return < date.today():
                user.is_block = True
                user.save()

                raise serializers.ValidationError("User blocked")

        copy = get_object_or_404(Copy, id=self.kwargs.get("pk"))

        if copy.copyNumber == 0:
            book = copy.book
            book.is_available = False
            book.save()

            raise serializers.ValidationError("Sem copias restantes")

        copy.copyNumber -= 1

        copy.save()

        serializer.save(expected_return=returnDate, user=user, copy=copy)


class LoanViewUpdate(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_url_kwarg = 'pk'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     instance_user = get_object_or_404(User, id=self.request.user.id)

    def perform_update(self, request: Request):
        queryset = Loan.objects.get(id=self.kwargs.get("pk"))
        user = self.request.user
        users = User.objects.all()
        copys = Copy.objects.all()

        for copy in copys:
            if copy.id == self.kwargs.get("pk"):
                if copy.copyNumber == 0:
                    book = get_object_or_404(Book, id=copy.book)
                    book.is_avaliable = True
                    book.save()

                copy.copyNumber += 1
                copy.save()

                break

        for user in users:
            if queryset.returnDate < date.today():
                user.is_block = True
                user.save()

                break

        loan = get_object_or_404(Loan, id=copy.id)

        loan.return_date = date.today()
        loan.save()

        serializer = LoanSerializer(loan)

        return Response(serializer.data, 200)
