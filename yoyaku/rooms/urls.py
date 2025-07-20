from django.urls import include, path
from rest_framework import routers

from .views import RoomsViewSet

router = routers.DefaultRouter()
router.register(r"", RoomsViewSet)

urlpatterns = [path("", include(router.urls))]
