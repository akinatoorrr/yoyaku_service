
def test_date_validation(api_client, create_room):
    response = api_client.post('/bookings/', {
        'room': create_room.id,
        'date_start': '2025-12-15',
        'date_end': '2025-12-10'
    }, format='json')
    assert response.status_code == 400
    assert 'Дата начала должна быть раньше даты окончания.' in str(response.content)
