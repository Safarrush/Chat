from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny
from users.models import User
from djoser.views import UserViewSet
from .serializers import UserRegistrSerializer, ProfileSerializer, MeSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.utils import BaseExcludePutMethodViewSet
from rest_framework.decorators import action, api_view, permission_classes


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer


class UserViewSet(BaseExcludePutMethodViewSet):
    queryset = User.objects.all()
    lookup_field = 'username'
    serializer_class = ProfileSerializer
    search_fields = ('=username',)
    permission_classes = (IsAuthenticated,)

    @action(
        methods=('get', 'patch'),
        detail=False,
        url_path='me',
        permission_classes=(IsAuthenticated,),
        serializer_class=MeSerializer
    )
    def users_profile(self, request):
        user = request.user
        if request.method == 'GET':
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
