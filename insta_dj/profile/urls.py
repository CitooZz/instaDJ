from rest_framework import routers
from django.conf.urls import include, url

from .api import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]
