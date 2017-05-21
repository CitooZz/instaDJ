from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from .utils import image_upload_handler


class Post(models.Model):
    creator = models.ForeignKey(User, related_name='posts')
    caption = models.CharField(max_length=50)
    image = models.ImageField(upload_to=image_upload_handler)

    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.caption

    @staticmethod
    def get_number_of_likes(self):
        return self.reaction.filter(type=PostReaction.LIKE)

    @staticmethod
    def get_number_of_dislikes(self):
        return self.reaction.filter(type=PostReaction.DISLIKE)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=150)

    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.comment


class PostReaction(models.Model):
    LIKE = 'Like'
    DISLIKE = 'Dislike'

    REACTION_TYPES = [LIKE, DISLIKE]

    post = models.ForeignKey(Post, related_name='reaction')
    user = models.ForeignKey(User)

    type = models.CharField(max_length=10, choices=zip(
        REACTION_TYPES, REACTION_TYPES))

    def __unicode__(self):
        return "{}: {} {}".format(self.type, self.user.username, self.post.caption)
