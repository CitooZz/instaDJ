from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from imagekit.models import ProcessedImageField


class Post(models.Model):
    creator = models.ForeignKey(get_user_model(), related_name='posts')
    caption = models.CharField(max_length=50)
    image = ProcessedImageField(
        upload_to="posts", format='JPEG', options={'quality': 100})

    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.caption

    @staticmethod
    def get_number_of_likes(self):
        return self.reaction.filter(type='Like')

    @staticmethod
    def get_number_of_dislikes(self):
        return self.reaction.filter(type='Dislike')


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    user = models.ForeignKey(get_user_model())
    comment = models.CharField(max_length=150)

    created_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.comment


REACTION_TYPES = ['Like', 'Dislike']


class LikeDislike(models.Model):
    post = models.ForeignKey(Post, related_name='reaction')
    user = models.ForeignKey(get_user_model())

    type = models.CharField(max_length=10, choices=zip(
        REACTION_TYPES, REACTION_TYPES))

    def __unicode__(self):
        return "{}: {} {}".format(self.type, self.user.username, self.post.caption)
