from django.urls import include, path
from rest_framework import routers

from .views import BookingsViewSet

router = routers.DefaultRouter()
router.register(r"", BookingsViewSet, basename="bookings")

urlpatterns = [path("", include(router.urls))]
