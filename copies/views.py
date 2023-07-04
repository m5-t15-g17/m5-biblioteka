from copies.serializers import CopySerializer
from .models import Copy
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListCreateAPIView

class CopyView(ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
