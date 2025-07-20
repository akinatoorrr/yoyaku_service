from datetime import date, datetime, timedelta

import pytest
from bookings.models import BookingModel
from rest_framework.test import APIClient
from rooms.models import RoomModel


@pytest.fixture
def create_room(db):
    room = RoomModel.objects.create(
        room_number=1, description="Cool room", price_per_night=1000
    )
    return room


@pytest.fixture
def create_booking(db, create_room):
    booking = BookingModel.objects.create(
        date_start="2025-12-10", date_end="2025-12-15", room=create_room
    )
    return booking


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def many_rooms(db):
    now = datetime.now()
    return [
        RoomModel.objects.create(
            room_number=i,
            price_per_night=1000 + i * 100,
            created_at=now - timedelta(days=i),
        )
        for i in range(10)
    ]


@pytest.fixture
def many_bookings(many_rooms):
    bookings = []
    for i in range(len(many_rooms)):
        bookings.append(
            BookingModel.objects.create(
                room=many_rooms[0],
                date_start=date.today() + timedelta(days=i),
                date_end=date.today() + timedelta(days=i + 1),
            )
        )
    return bookings
