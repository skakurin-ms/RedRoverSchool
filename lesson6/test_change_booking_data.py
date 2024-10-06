from home_task_6 import *
from data.urls import urls

def test_change_booking_data():
    response_create = create_booking()
    response_change = change_reservation_data(response_create.json()["bookingid"])
    response_get = get_booking_by_id(response_create.json()["bookingid"])
    assert(response_change.json()["firstname"], response_change.json()["lastname"]) == (response_get.json()["firstname"], response_get.json()["lastname"])
