from rest_framework import serializers

from .models import BookingModel


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = ('id', 'date_start', 'date_end', 'room')
        read_only_fields = ('id', 'created_at')

    def validate(self, data):
        if data['date_start'] >= data['date_end']:
            raise serializers.ValidationError(
                'Дата начала должна быть раньше даты окончания.'
            )
        return data
