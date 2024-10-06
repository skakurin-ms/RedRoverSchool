from home_task_6 import *
from data.urls import urls

def test_create_booking():
    response_create = create_booking()
    response_get = get_booking_by_id(response_create.json()["bookingid"])
    assert(response_create.json()["booking"]["firstname"], response_create.json()["booking"]["lastname"]) == (response_get.json()["firstname"], response_get.json()["lastname"])
