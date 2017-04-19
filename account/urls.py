from rest_framework import routers
from django.conf.urls import include, url

from account.api import (
    UserViewSet
)

router = routers.DefaultRouter()
router.register(r'', UserViewSet)


urlpatterns = [
    url(r'^', include(router.urls))
]
