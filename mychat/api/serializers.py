from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from users.models import User


class UserRegistrSerializer(UserCreateSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'first_name',
            'last_name',
            'password',
        )