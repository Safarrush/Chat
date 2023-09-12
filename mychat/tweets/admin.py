from django.contrib import admin

from .models import Tweet, TweetLike


<<<<<<< HEAD
# class TweetLikeAdmin(admin.TabularInline):
# model = TweetLike
=======
class TweetLikeAdmin(admin.TabularInline):
    model = TweetLike
>>>>>>> 75b76978d444b14f962f0675f8f065e0d7d09536


@admin.register(Tweet)
class UserAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    # inlines = [TweetLikeAdmin]
    list_display = (
        '__str__',
        #     'user',
    )
   # search_fields = ['content', 'user__username', 'user__email']
=======
    inlines = [TweetLikeAdmin]
    list_display = (
        '__str__',
        'user',
    )
    search_fields = ['content', 'user__username', 'user__email']
>>>>>>> 75b76978d444b14f962f0675f8f065e0d7d09536
    list_filter = ('content',)

    class Meta:
        model = Tweet
