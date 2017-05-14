from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ProcessedImageField


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    followers = models.ManyToManyField(User, related_name='followers')
    following = models.ManyToManyField(User, related_name='following')

    avatar = ProcessedImageField(upload_to='avatar', options={
        'quality': 100}, null=True, blank=True)

    description = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
