
from bookings.models import BookingModel
from rooms.models import RoomModel


def test_create_room_and_booking(create_room, create_booking):
    assert RoomModel.objects.count() == 1
    assert BookingModel.objects.count()  == 1
    assert create_booking in create_room.bookings.all()

def test_cascade_delete(create_room, create_booking):
    create_room.delete()
    assert BookingModel.objects.count() == 0
