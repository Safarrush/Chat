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


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'bio', 'role',
        )
        model = User


class MeSerializer(ProfileSerializer):

    class Meta(ProfileSerializer.Meta):
        read_only_fields = ('role',)
