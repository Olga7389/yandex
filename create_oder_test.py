import sender_stand_request


#Проверка кода 200
def test_get_order():
    track = sender_stand_request.get_new_track()
    track = sender_stand_request.get_order_body(track)
    assert track.status_code == 200