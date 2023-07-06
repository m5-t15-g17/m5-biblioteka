from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from books.models import Book
from books.serializers import BookSerializer
from users.permissions import IsAdmin


class BookView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def post(self, request, *args, **kwargs):
    #     return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class BookDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmin]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "pk"
