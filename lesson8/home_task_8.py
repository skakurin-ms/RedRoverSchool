#task 1
# def is_lucky_ticket(ticket_id: int):
#     """
#         Проверяет, является ли билет счастливым.
#
#         Счастливым считается билет, у которого сумма первых трех цифр
#         серийного номера равна сумме последних трех цифр.
#
#         Аргументы:
#         ticket_id (int): Серийный номер билета, должен быть шестизначным целым числом.
#
#         Исключения:
#         TypeError: Если ticket_id не является целым числом.
#         ValueError: Если ticket_id не является шестизначным числом.
#
#         Возвращает:
#         bool: True, если билет счастливый, иначе False.
#         """
#     if type(ticket_id) != int:
#         raise TypeError("неверный тип данных для ticket_id, ticket_id должен быть целым числом")
#     ticket_id_to_str = str(ticket_id)
#     if len(ticket_id_to_str) != 6:
#         raise ValueError("некорректная длина для ticket_id, ticket_id должен быть шестизначным числом")
#
#     summ1 = sum([int(i) for i in ticket_id[:3]])
#     summ2 = sum([int(i) for i in ticket_id[3:]])
#
#     return summ1 != summ2
#
# is_lucky_ticket(432341)

# #task 2
# def is_armstrong_number():
#     armstrong_digits = []
#     for i in range(100, 1001):
#         number_split = [int(digit) for digit in str(i)]
#         if sum(map(lambda digit: pow(digit, 3), number_split)) == i:
#             armstrong_digits.append(i)
#     print("Числа армcтронга:", armstrong_digits)
#     return None
#
# is_armstrong_number()

#task 3
# def censor_print(string_: str):
#     censored_list = ["козел", "баран", "овца"]
#     for word in censored_list:
#         string_ = string_.replace(word, "***")
#     print(string_)
#
# censor_print("этот баран и овца и этот козел тоже должны быть в общем загоне для животных ")


#task 4
flashcards = {
    "city" : {
        "building": "здание",
        "street": "улица",
        "park": "парк",
        "bridge": "мост",
        "traffic": "движение"
    },
    "fruits" : {
        "apple": "яблоко",
        "banana": "банан",
        "orange": "апельсин",
        "grape": "виноград",
        "strawberry": "клубника"
    }
}

while True:
    user_answer = input(f"Привет! Выбери сегодняшнюю тему для изучения: '{ ','.join(list(flashcards.keys()))}' или введи 'выйти': ")
    if user_answer == "выйти":
        print("Но ты приходи еще!")
        break
    elif user_answer in flashcards:
        correct_answers = 0
        questions_amount = 0
        for word in flashcards[user_answer]:
            questions_amount += 1
            user_translation = input(f"Введите перевод для слова {word}: ")
            if user_translation == flashcards[user_answer][word]:
                print("Верно!")
                correct_answers += 1
            else:
                print(f"Неверно! Правильный перевод: {flashcards[user_answer][word]}")
    print(f"Ты набрал {correct_answers}  правильных овтетов из {questions_amount} вопросов")




