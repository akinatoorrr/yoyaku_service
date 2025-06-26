from rest_framework import mixins, viewsets

from .models import BookingModel
from .serializers import BookingSerializer


class BookingsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                   mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = BookingSerializer
    http_method_names = ('get', 'post', 'delete')

    def get_queryset(self):
        queryset = BookingModel.objects.all()
        room_id = self.request.query_params.get('room_id')
        if room_id is not None:
            queryset = queryset.filter(room_id=room_id)
        return queryset
