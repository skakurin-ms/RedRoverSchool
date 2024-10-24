# def decor(func):
#     def wrapper():
#         print("Before func call...")
#         func()
#         print("After func call...")
#     return wrapper
#
# @decor
# def hello_world():
#     print("Hello World!")
#
# hello_world()
#
#вариант записи без декоратора
# def decor(func):
#     def wrapper():
#         print("Before func call...")
#         func()
#         print("After func call...")
#     return wrapper
#
#
# def hello_world():
#     print("Hello World!")
#
# result_of_call = decor(hello_world)
# result_of_call()