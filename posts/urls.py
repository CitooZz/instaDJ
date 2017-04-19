from rest_framework import routers
from django.conf.urls import include, url

from posts.api import (
    PostViewSet
)

router = routers.DefaultRouter()
router.register(r'', PostViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]
