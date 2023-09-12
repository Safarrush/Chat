from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from users.models import User
from django.contrib.contenttypes.fields import GenericRelation


class TweetLike(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='likes')
    # timestamp = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Tweet(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    likes = GenericRelation(TweetLike)
    timestamp = models.DateTimeField(auto_now_add=True)
    # image = models.FileField(upload_to='images/', blank=True)

    class Meta:
        ordering = ['-id']

    @property
    def total_likes(self):
        return self.likes.count()
