from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Notification(models.Model):
    actor = models.ForeignKey(User, related_name='notification_actors')
    target = models.ForeignKey(User, related_name='notifications')

    content_type = models.ForeignKey(
        ContentType, related_name='content_type_set_for_%(class)s')

    object_pk = models.PositiveIntegerField('object ID')
    object = GenericForeignKey(ct_field='content_type', fk_field='object_pk')
