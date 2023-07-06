from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from .permissions import IsAccountOwner, IsAdmin
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def post(self, request: Request, *args, **kwargs):
    #     return super().post(request, *args, **kwargs)
   

class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated , IsAdmin | IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = 'pk'

    
