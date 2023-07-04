from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from books.models import Book
from books.serializers import BookSerializer


class BookView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # def post(self, request, *args, **kwargs):
    #     return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
