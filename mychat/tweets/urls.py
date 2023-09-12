from django.contrib import admin
from django.urls import include, path

from .views import tweet_delete_view, tweet_action_view, tweet_create_view, tweet_list_view, tweet_detail_view, TweetViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'posts', TweetViewSet)

urlpatterns = [
    path('', tweet_list_view, name='tweets'),
    path('action/', tweet_action_view, name='tweet_action'),
    path('create/', tweet_create_view, name='create'),
    path('<int:tweet_id>/delete/', tweet_delete_view, name='delete'),
    path('<int:tweet_id>/', tweet_detail_view, name='detail'),
]

urlpatterns = router.urls
