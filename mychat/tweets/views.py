from django.shortcuts import render
from .models import Tweet
from .serializers import TweetSerializer, TweetActionSerializer, TweetCreateSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import filters, status
from rest_framework.permissions import (SAFE_METHODS, AllowAny,
                                        IsAuthenticated)
<<<<<<< HEAD
from rest_framework import viewsets
from .mixins import LikedMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
=======
>>>>>>> 75b76978d444b14f962f0675f8f065e0d7d09536
# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        obj = serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    queryset = Tweet.objects.filter(id=tweet_id)
    if not queryset.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TweetSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_action_view(request, *args, **kwargs):
    serializer = TweetActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get('id')
        action = data.get('action')
        content = data.get('content')
        queryset = Tweet.objects.filter(id=tweet_id)
        if not queryset.exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        obj = queryset.first()
        if action == 'like':
            obj.likes.add(request.user)
            serializer = TweetSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif action == 'unlike':
            obj.likes.remove(request.user)
            serializer = TweetSerializer(obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif action == 'retweet':
            new_tweet = Tweet.objects.create(
                user=request.user,
                parent=obj,
                content=content,
            )
            serializer = TweetSerializer(new_tweet)
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    queryset = Tweet.objects.filter(id=tweet_id)
    if not queryset.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    queryset = queryset.filter(user=request.user)
    if not queryset.exists():
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    obj = queryset.first()
    obj.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    queryset = Tweet.objects.all()
<<<<<<< HEAD
    username = request.GET.get('username')
    if username != None:
        queryset = queryset.filter(user__username__iexact=username)
    serializer = TweetSerializer(queryset, many=True)
    return Response(serializer.data)


class TweetViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
=======
    serializer = TweetSerializer(queryset, many=True)
    return Response(serializer.data)
>>>>>>> 75b76978d444b14f962f0675f8f065e0d7d09536
