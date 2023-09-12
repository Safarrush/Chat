from django.db import models
<<<<<<< HEAD
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from users.models import User
from django.contrib.contenttypes.fields import GenericRelation


class TweetLike(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='likes')
    # tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    # timestamp = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # class Meta:
    # verbose_name = 'Лайк'
    # verbose_name_plural = 'Лайки'
    # constraints = [
    # models.UniqueConstraint(
    # fields=['user', 'tweet'],
    # name='unique_like'
    # )
    #  ]

   # def __str__(self):
    # return f'{self.user} поставил лайк {self.tweet}'


class Tweet(models.Model):
    # parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    # likes = models.ManyToManyField(
    # User, related_name='tweet_user', blank=True, through=TweetLike)
    likes = GenericRelation(TweetLike)
    timestamp = models.DateTimeField(auto_now_add=True)
    # image = models.FileField(upload_to='images/', blank=True)
=======

from users.models import User


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    parent = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    likes = models.ManyToManyField(
        User, related_name='tweet_user', blank=True, through=TweetLike)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='images/', blank=True)
>>>>>>> 75b76978d444b14f962f0675f8f065e0d7d09536

    class Meta:
        ordering = ['-id']

    @property
<<<<<<< HEAD
    # def is_retweet(self):
    # return self.parent != None
    def total_likes(self):
        return self.likes.count()
=======
    def is_retweet(self):
        return self.parent != None
>>>>>>> 75b76978d444b14f962f0675f8f065e0d7d09536
