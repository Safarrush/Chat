from api.views import CustomUserViewSet
from django.urls import include, path
from rest_framework import routers
from tweets.views import tweet_create_view, tweet_list_view

router = routers.DefaultRouter()
router.register('users', CustomUserViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls))
]
