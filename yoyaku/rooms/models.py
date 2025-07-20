from django.db import models


class RoomModel(models.Model):
    room_number = models.IntegerField(unique=True, verbose_name="номер комнаты")
    description = models.CharField(max_length=150, verbose_name="описание номера")
    price_per_night = models.PositiveIntegerField(verbose_name="цена номера за ночь")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="дата добавления номера"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="дата изменения номера"
    )

    class Meta:
        verbose_name = "номер"
        verbose_name_plural = "номера"
        ordering = ("room_number",)

    def __str__(self):
        return f"Номер {self.room_number}"
