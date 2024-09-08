# task1
#solution 1
# lst = []
# for digit in range(0, 101):
#     if digit % 2 == 0 and digit % 3 == 0:
#         lst.append(digit)
# print(lst)

#solution 2
# lst = [digit for digit in range(0, 101) if digit % 2 == 0 and digit % 3 == 0]
# print(lst)

# task2
# items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# numbers = []
# for item in items:
#     if isinstance(item, (int, float)):
#         numbers.append(item)
# print(sum(numbers))

# task3
# message = []
# while True:
#     string = input("Введите строку: ")
#     message.append(string)
#     if len(message) > 5:
#         message.pop(0)
#
#     if string == "Пока":
#         print("Ну ладно, пока!")
#         print(message)
#         break

# task 4
#solution 1
# numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
# print(sorted(list(set(numbers))))

#solution 2
# numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
# lst = []
# for item in numbers:
#     if item in lst:
#         continue
#     else:
#         lst.append(item)
# print(sorted(lst))

# Рефакторинг:
'''
1.В условии сравнения вместо and должен быть оператор or (так как задание
подразумевает условие ИЛИ (выполнение одного из условий)
2.Сообщение о предоставлении доступа перепутан местами
'''
import string

#Словари
# task1
# summ_cost = 0
# products = {
# "apple": {"quantity": 10, "price": 100},
# "banana": {"quantity": 20, "price": 50},
# "orange": {"quantity": 15, "price": 80},
# "grape": {"quantity": 8, "price": 120},
# "milk":{"quantity": 12, "price": 90},
# "bread": {"quantity": 30, "price": 40}
# }
#
# del products["milk"]
#
# for key in products.keys():
#     products[key]["price"] += (products[key]["price"] * 20) / 100
#
# products["Salt"] = {"quantity": 7, "price": 12}
#
# for key in products.keys():
#     summ_cost += products[key]["price"] * products[key]["quantity"]
#
# print(summ_cost)

#task 2
# keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education',
# 'company', 'salary']
#
# values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890',
# 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]
#
# info = {}
# info = {key: value for key, value in zip(keys, values)} #через генератор
# for item in range(len(keys)):
#     info[keys[item]] = values[item]
# print(info)
#
# task 3
# message = "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"
# length = len(message)
# decode = ""
#
# cipher = {
# "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
# "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
# "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
# "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
# "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
# }
#
# for char in message:
#     if char in cipher:
#         decode += cipher[char]
# print(decode)
#
# answer = input("Введите сообщение-ответ: ")
# encode_answer = ""
#
# for char in answer:
#     if char not in cipher.values():
#         encode_answer += char
#     else:
#         for key, value in cipher.items():
#             if char == value:
#                 encode_answer += key
#                 break
# print("Зашифрованное сообщение =", encode_answer)

#task 4
# dialog = """Doc: Запомни! Согласно моей теории, ты помешал знакомству
# своих родителей.
# Если они не встретятся, то не влюбятся, не поженятся, и у них не будет детей.
# Поэтому твой старший брат исчезает с фотографии. Затем очередь твоей
# сестры,
# и если ты все не исправишь, ты будешь следующим.
# Marty: Тяжелый случай.
# Doc: Вес тут совершенно ни при чем. """
# dlg = dialog.lower()
# dct = {}
# count = 0
# for char in dlg:
#     if char not in (string.punctuation + string.ascii_lowercase + " ") and char not in dct:
#         dct[char] = dlg.count(char)
# print(dct)
# print(f"key = {max(dct, key=dct.get)}\nvalue = {max(dct.values())}") #
