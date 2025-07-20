from rest_framework import serializers

from .models import BookingModel


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = ("id", "date_start", "date_end", "room")
        read_only_fields = ("id", "created_at")

    def validate(self, data):
        if data["date_start"] >= data["date_end"]:
            raise serializers.ValidationError(
                "Дата начала должна быть раньше даты окончания."
            )
        qs = BookingModel.objects.filter(
            room=data["room"],
            date_start__lt=data["date_end"],
            date_end__gt=data["date_start"],
        )
        if qs.exists():
            raise serializers.ValidationError(
                "Номер уже забронирован в указанный период."
            )
        return data
