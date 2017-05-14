from rest_framework import viewsets
from rest_framework import permissions

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = PostSerializer
    queryset = Post.objects.none()

    def get_queryset(self):
        return Post.objects.filter(creator=self.request.user)
