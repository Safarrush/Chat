from django.contrib import admin
from django.urls import include, path

from .views import TweetViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'posts', TweetViewSet)


urlpatterns = router.urls
