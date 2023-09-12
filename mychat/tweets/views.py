from django.shortcuts import render
from .models import Tweet
from .serializers import TweetSerializer, TweetActionSerializer, TweetCreateSerializer, TweetAuthorSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import filters, status
from rest_framework.permissions import (SAFE_METHODS, AllowAny,
                                        IsAuthenticated)
from rest_framework import viewsets
from .mixins import LikedMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
# Create your views here.


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


class TweetViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[IsAuthenticated],
        url_path='my'
    )
    def get_user_tweets(self, request):
        user = self.request.user
        tweets = Tweet.objects.filter(user=user)
        serializer = self.get_serializer(tweets, many=True)
        return Response(serializer.data)
