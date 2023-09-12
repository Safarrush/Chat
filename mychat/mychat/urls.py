from django.contrib import admin
from django.urls import include, path

from tweets.views import tweet_delete_view, tweet_action_view, tweet_create_view, tweet_list_view, tweet_detail_view
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweets/', tweet_list_view, name='tweets'),
    path('create/', tweet_create_view, name='create'),
    path('react/', TemplateView.as_view(template_name='react.html')),
<<<<<<< HEAD
    path('api/profile/', include('users.urls')),
    path('api/vsas/', include('tweets.urls')),
=======
    # path('tweets/action', tweet_action_view, name='tweet_action'),
    # path('tweets/<int:tweet_id>/delete', tweet_delete_view, name='delete'),
    # path('tweets/<int:tweet_id>', tweet_detail_view, name='detail'),
    path('api/tweets/', include('tweets.urls')),
>>>>>>> 75b76978d444b14f962f0675f8f065e0d7d09536
    path('api/', include('api.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
