from rest_framework import mixins, viewsets

from .models import BookingModel
from .serializers import BookingSerializer


class BookingsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                   mixins.DestroyModelMixin, viewsets.GenericViewSet):
    serializer_class = BookingSerializer
    http_method_names = ('get', 'post', 'delete')

    def get_queryset(self):
        room_id = self.request.query_params.get('room_id')
        return BookingModel.objects.filter(room=room_id)
