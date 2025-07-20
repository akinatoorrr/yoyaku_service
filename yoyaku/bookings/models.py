from django.db import models
from rooms.models import RoomModel


class BookingModel(models.Model):
    date_start = models.DateField(verbose_name="начало бронирования")
    date_end = models.DateField(verbose_name="конец бронирования")
    room = models.ForeignKey(
        RoomModel, on_delete=models.CASCADE, related_name="bookings"
    )

    class Meta:
        verbose_name = "бронирование"
        verbose_name_plural = "бронирования"
        ordering = ("date_start",)

    def __str__(self):
        return str(self.id)
