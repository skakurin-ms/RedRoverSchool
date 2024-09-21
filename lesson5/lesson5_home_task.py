# task 1
# class Rectangle:
#     def __init__(self, weight: int, height: int):
#         self.weight = weight
#         self.height = height
#     def area(self):
#         return self.weight * self.height
#     def perimeter(self):
#         return self.weight + self.height
#
# rect = Rectangle(2, 4)
# a = rect.area()
# print("Area: ", a)# Вернул 8
# p = rect.perimeter()
# print("Perimeter: ", p) # Вернул 6

# task 2
# class Car:
#     def __init__(self, make: str, max_speed: int):
#         self.speed = 0
#         self.make = make
#         self.max_speed = max_speed
#     def display_speed(self):
#         print("Current speed: ", self.speed)
#
#     def accelerate(self):
#         if self.speed + 10 <= self.max_speed:
#             self.speed += 10
#         return self.speed
#
#     def brake(self):
#         if self.speed - 10 >= 0:
#             self.speed -= 10
#         return self.speed
#
# my_toyota = Car("Toyota", 180)
# my_toyota.accelerate()
# my_toyota.accelerate()
# my_toyota.accelerate()
# my_toyota.display_speed()

# task 3
# class BankAccount:
#     def __init__(self, name: str, balance: int):
#         self._name = name
#         self._balance = balance
#
#     def deposit(self, amount: int):
#         self._balance += amount
#
#     def withdraw(self, amount: int):
#         if self._balance - amount <= 0:
#             print("Недостаточно средств!")
#         else:
#             self._balance -= amount
#
#     def get_balance(self):
#         return self._balance
#
# account = BankAccount("Maria", 1000)
# account.deposit(700)
# account.withdraw(200)
# print(account.get_balance())
#
#
# # task 4
# class OverdraftAccount(BankAccount):
#     def withdraw(self, amount: int):
#         self._balance -= amount

# jack_account = OverdraftAccount("Jack", 0)
# jack_account.withdraw(100)
#
# jack_account.withdraw(100)
# jack_account.withdraw(100)
# print(jack_account.get_balance())

