import re
import string
#
# class RegistrationError(Exception):
#     pass
# #
# # # task 1
# def registration(username: str, password: str):
#     if not isinstance(username, str) or not (4 <= len(username) <= 15) or not username.isalpha():
#         raise RegistrationError(f"Введенны некорректные данные")
#
#     if not (8 <= len(password) <= 45) or not username.isalnum():
#         raise RegistrationError(f"Введенны некорректные данные")
#     return True
#
# # task 2
# def request_username_password():
#     while True:
#         username = input("Введите username: ")
#         password = input("Введите password: ")
#         try:
#             registration(username, password)
#             print("Успешно")
#             break
#         except RegistrationError as error:
#             print("Ошибка регистрации!", error)
#
# request_username_password()

#task #3
# def request_action():
#     while True:
#         action = input("Введите действие одной из действий (прочитать, записать, выйти): ")
#         if action == "прочитать":
#             with open("journal.txt", "r") as file:
#                 print(file.read())
#         elif action == "записать":
#             line = input("Введите строку для записи: ")
#             with open("journal.txt", "a") as file:
#                 file.write("\n" + line)
#         elif action == "выйти":
#             print("Ещё увидимся!")
#             break
# request_action()

def func1(a, b):
    func2 = lambda a, b: a+ b
    return func2(a, b)