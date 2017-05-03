from rest_framework import serializers
from posts.models import (
    Post
)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('pk', 'creator', 'caption', 'image', 'created_at')
        read_only_fields = ('creator', 'created_at')
