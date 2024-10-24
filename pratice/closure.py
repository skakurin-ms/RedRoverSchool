#simple closure
# def func(n):
#     m = 2
#     def closure():
#         print("Call from closure internal function: ", n)
#         return n * m
#     return closure
#
# call_func = func(4)
#
# print("Call function via variable: ", call_func())
# print("Call function directly: ", func(2)())

#closure with the same parameter
# def func(n):
#     m = 2
#     def closure(m=m):
#         print("Call from closure internal function: ", n)
#         return m * n
#     return closure
#
# print(func(3)())

#closure with 2 instances
# def func(m):
#     print("Call from parent function: ", m)
#     def closure(n):
#         print("Call from closure internal function: ", n)
#         return m * n
#     return closure
#
# instance_1 = func(3)
# print("instance 1: ", instance_1(4))
# print()
# instance_2 = func(10)
# print("instance 2: ", instance_2(5))


#closure as lambda
# def func(func_2):
#     return lambda x: func_2(x)
#
# result_of_call = func(lambda x: x * x)
# print("result_of_call: ", result_of_call(4))



