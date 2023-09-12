from api.views import CustomUserViewSet
from django.urls import include, path
from rest_framework import routers
from api.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', CustomUserViewSet)
router.register('profile', UserViewSet, basename='users')


urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls))
]
