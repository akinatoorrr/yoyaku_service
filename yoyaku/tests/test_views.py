import pytest
from bookings.models import BookingModel
from rooms.models import RoomModel


def test_get_rooms(api_client, many_rooms):
    response = api_client.get("/rooms/", format="json")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10


def test_get_bookings(api_client, many_bookings, many_rooms):
    room = many_rooms[0]
    response = api_client.get("/bookings/", {"room_id": room.id}, format="json")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 10


def test_create_room_and_booking(db, api_client):
    response = api_client.post(
        "/rooms/",
        {"room_number": 1, "price_per_night": 4000, "description": "luxury room"},
        format="json",
    )
    assert response.status_code == 201
    room_data = response.json()
    assert room_data["room_number"] == 1
    assert room_data["price_per_night"] == 4000
    assert RoomModel.objects.filter(id=room_data["id"]).exists()

    response = api_client.post(
        "/bookings/",
        {"date_start": "2025-12-10", "date_end": "2025-12-12", "room": room_data["id"]},
        format="json",
    )
    assert response.status_code == 201
    booking_data = response.json()
    assert booking_data["date_start"] == "2025-12-10"
    assert booking_data["date_end"] == "2025-12-12"
    assert booking_data["room"] == room_data["id"]


@pytest.mark.parametrize(
    "ordering_param",
    ["price_per_night", "-price_per_night", "created_at", "-created_at"],
)
def test_rooms_ordering(api_client, many_rooms, ordering_param):
    response = api_client.get(f"/rooms/?ordering={ordering_param}", format="json")
    assert response.status_code == 200
    data = response.json()
    is_desc = ordering_param.startswith("-")
    field = ordering_param.lstrip("-")
    values = [room[field] for room in data]
    assert values == sorted(values, reverse=is_desc)


def test_delete_rooms(api_client, create_room):
    response = api_client.delete(f"/rooms/{create_room.id}/")
    assert response.status_code == 204
    assert RoomModel.objects.count() == 0


def test_delete_bookings(api_client, create_booking):
    response = api_client.delete(f"/bookings/{create_booking.id}/")
    assert response.status_code == 204
    assert BookingModel.objects.count() == 0
