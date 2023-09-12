from django.contrib import admin
from django.urls import include, path

<<<<<<< HEAD
from .views import tweet_delete_view, tweet_action_view, tweet_create_view, tweet_list_view, tweet_detail_view, TweetViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'posts', TweetViewSet)
=======
from .views import tweet_delete_view, tweet_action_view, tweet_create_view, tweet_list_view, tweet_detail_view
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('tweets', tweet_list_view, basename='tweet_list')
# router.register('tweets/<int:tweet>', tweet_detail_view)
>>>>>>> 75b76978d444b14f962f0675f8f065e0d7d09536

urlpatterns = [
    path('', tweet_list_view, name='tweets'),
    path('action/', tweet_action_view, name='tweet_action'),
    path('create/', tweet_create_view, name='create'),
    path('<int:tweet_id>/delete/', tweet_delete_view, name='delete'),
    path('<int:tweet_id>/', tweet_detail_view, name='detail'),
]
<<<<<<< HEAD

urlpatterns = router.urls
=======
>>>>>>> 75b76978d444b14f962f0675f8f065e0d7d09536
