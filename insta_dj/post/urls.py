from rest_framework import routers
from django.conf.urls import include, url

from .api import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]
