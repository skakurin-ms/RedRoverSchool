from home_task_6 import *
from data.urls import urls

def test_remove_booking_data():
    response_create = create_booking()
    response_remove = remove_booking_by_id(response_create.json()["bookingid"])
    assert get_booking_by_id(response_create.json()["bookingid"]).status_code == 404