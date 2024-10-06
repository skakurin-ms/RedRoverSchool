import requests
from pprint import pprint
from data.urls import urls


def get_token():
    credentials = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(urls.URL_TOKEN, json=credentials)
    print(response.json())
    return response.json()["token"]
# task # 1
def get_all_booking_ids():
    response = requests.get(urls.URL)
    return response

def create_booking():
    data = {
        "firstname": "Sergey",
        "lastname": "Kakurin",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(urls.URL, json=data)
    print("Booking created...", response.json())
    # print(response.json())
    # assert response.status_code == 200
    return response

def get_booking_by_id(id_):
    response = requests.get(urls.URL + "/" + str(id_))
    print(f"Info about booling by {id_}:")
    # pprint(response.json())
    # assert(response.json()["firstname"], response.json()["lastname"]) == ("Sergey", "Kakurin")
    return response

def change_reservation_data(booking_id):
    new_data = {
        "firstname": "Pawel",
        "lastname": "Komash"
    }

    headers = {
        "Cookie": f"token={get_token()}"
    }
    response = requests.patch(urls.URL + "/" + str(booking_id), data=new_data, headers=headers)
    print("Data changed: ")
    print(response.json())
    return response
def remove_booking_by_id(booking_id):
    headers = {
        "Cookie": f"token={get_token()}"
    }
    response = requests.delete(urls.URL + "/" + str(booking_id), headers=headers)
    print("Data removed: ")
    print(response.status_code)
    return response


pprint(get_all_booking_ids())
response = create_booking()
my_id = response.json()["bookingid"]
print("My booking id: ", my_id)
change_reservation_data(my_id)
response = get_booking_by_id(my_id)
pprint(response.json())
remove_booking_by_id(my_id)




# class Calculator:
#     def __init__(self):
#         self.history = []
#     def add(self, a, b):
#         self.history.append(str(f"{a} + {b} = {a + b}"))
#         return f"{a} + {b} = {a + b}"
#     def mul(self, a, b):
#         self.history.append(str(f"{a} * {b} = {a * b}"))
#         return f"{a} * {b} = {a * b}"
#     def div(self, a, b):
#         self.history.append(str(f"{a} / {b} = {a / b}"))
#         return f"{a} / {b} = {a / b}"
#     def show_operations(self):
#         for operation in self.history:
#             print(operation)
#         return self.history
#
#     def clear(self):
#         return self.history.clear()
#
#
# calc = Calculator()
# calc.add(1, 3)
# calc.add(2, 10)
# calc.mul(100, 12.2)
# calc.show_operations()

