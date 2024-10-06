from home_task_6 import *
from data.urls import urls

def test_get_all_booking_ids():
    response = get_all_booking_ids()
    assert response.status_code == 200