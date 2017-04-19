from rest_framework import viewsets
from rest_framework import permissions

from posts.models import (
    Post
)

from posts.serializers import (
    PostSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = PostSerializer
    queryset = Post.objects.none()

    def get_queryset(self):
        return Post.objects.filter(creator=self.request.user)
