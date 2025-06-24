from rest_framework import mixins, viewsets
from rest_framework.filters import OrderingFilter

from .models import RoomModel
from .serializers import RoomSerializer


class RoomsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                   mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = RoomModel.objects.all()
    serializer_class = RoomSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('price_per_night', 'created_at')
    http_method_names = ('get', 'post', 'delete')
