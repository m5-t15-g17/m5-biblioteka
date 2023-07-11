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
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import pdb
from datetime import timedelta
from django.forms import model_to_dict


class LoanView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = "pk"

    print("1")
    # pdb.set_trace()
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    print("2")

    # pdb.set_trace()
    def get_queryset(self):
        print("3")
        # pdb.set_trace()
        queryset = super().get_queryset()
        instance_user = get_object_or_404(User, id=self.request.user.id)
        print("4")
        # pdb.set_trace()

        return queryset.filter(users=instance_user)
    
    # def post(self, request, *args, **kwargs):
    #     print("estou no post")
    #     user = get_object_or_404(User, id=self.request.user.id)
    #     return super().post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("estou no post")
        user = get_object_or_404(User, id=self.request.user.id)

        # if user.is_block:
        #     print("estou no post2")
        #     return Response({"error": "User blocked"})
        # loans = user.loans.all()

        # for loan in loans:
        #     print("estou no post3")
        #     if loan.return_date < datetime.now():
        #         serializer = UserSerializer(user, {"is_block": True}, partial=True)
        #         print("estou no post4")
        #         serializer.is_valid(raise_exception=True)
        #         serializer.save()
        #         print("estou no post5")
        #         return Response({"error": "User blocked"})
        # return super().post(request, *args, **kwargs)
        return Response({"message":"Emprestimo feito com sucesso"})
    def perform_create(self, serializer):
        returnDate = datetime.now()
        returnDate = returnDate + timedelta(7, 0)

        user = get_object_or_404(User, id=self.request.user.id)
        if user.is_block:
            print("estou no post2")
            return Response({"error": "User blocked"})
        loans = user.loans.all()

        for loan in loans:
            print("estou no post3")
            if loan.return_date < datetime.now():
                serializer = UserSerializer(user, {"is_block": True}, partial=True)
                print("estou no post4")
                serializer.is_valid(raise_exception=True)
                serializer.save()
                print("estou no post5")
                return Response({"error": "User blocked"})
        copy = get_object_or_404(Copy, id=self.kwargs.get("pk"))
        copys = Loan.objects.filter(copy=copy)
        print(user, "1", copy, "2", len(copys), "3", "////////////////////////")
        # pdb.set_trace()
        # for copy in copys:
        #     print(copy,"*******************************************")
        # pdb.set_trace()
        # if copy.id == self.kwargs.get("pk"):
        if copy.copyNumber == 0:
            book = get_object_or_404(Book, id=copy.book)
            serializer = BookSerializer(book, {"is_avaliable": False}, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response("no copies left", 400)

        serializer = CopySerializer(data=copy, partial=True)
        serializer.copyNumber = copy.copyNumber - 1
        serializer.is_valid(raise_exception=True)
        serializer.save()

        loanSerializer = LoanSerializer(copy=copy, expected_return=returnDate, user=user)
        loanSerializer.is_valid(raise_exception=True)

        # serializer.save(copy=copy, expected_return=returnDate, user=user)
        # break
        # copyDict = model_to_dict(serializer)

        # return Response(copyDict)
        return loanSerializer.save()

    # def perform_create(self, serializer):
    #     returnDate = datetime.datetime.now()
    #     returnDate = returnDate + datetime.timedelta(days=7)
    #     user = get_object_or_404(User, pk=self.request.user.id)
    #     copy = get_object_or_404(Copy, pk=self.kwargs.get("pk"))
    #     copys = copy.loan.all()
    #     for copy in copys:
    #         if copy.id == self.kwargs.get("pk"):
    #             if copy.copyNumber == 0:
    #                 book = get_object_or_404(Book, pk=copy.book.pk)
    #                 book.is_available = False
    #                 book.save()
    #                 return Response("no copies left", status=400)
    #             copy.copyNumber -= 1
    #             copy.save()
    #             break
    #     serializer.save(copy=copy, expected_return=returnDate, user=user)
    #     return Response(serializer.data, status=201)

    def patch(self, request: Request):
        user = get_object_or_404(User, id=self.request.user.id)

        self.check_object_permissions(request, user)
        loans = user.loan.all()
        copy = get_object_or_404(Copy, id=self.kwargs.get("pk"))
        copys = copy.loan.all()

        for copy in copys:
            if copy.id == self.kwargs.get("pk"):
                if copy.copyNumber == 0:
                    book = get_object_or_404(Book, id=copy.book)
                    serializer = BookSerializer(
                        book, {"is_avaliable": True}, partial=True
                    )
                    serializer.is_valid(raise_exception=True)
                    serializer.save()

                serializer = CopySerializer(
                    copy, {"copyNumber": "copyNumber" + 1}, partial=True
                )
                serializer.is_valid(raise_exception=True)
                serializer.save()

                break

        for loan in loans:
            if loan.return_date < datetime.now():
                serializer = UserSerializer(user, {"is_block": True}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                break

        loan = get_object_or_404(Loan, id=self.kwargs.get("loan_id"))

        setattr(loan, "return_date", datetime.now)

        loan.save()

        serializer = LoanSerializer(loan)

        return Response(serializer.data, 200)
