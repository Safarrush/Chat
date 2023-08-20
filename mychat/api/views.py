from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from users.models import User
from djoser.views import UserViewSet
from .serializers import UserRegistrSerializer
 
 
class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer