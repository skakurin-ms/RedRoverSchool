#task1
# solution 1
# def sum_ignore_non_numbers(items: list):
#     summ = 0
#     for item in items:
#         if isinstance(item, (int, float)):
#             summ += item
#     return summ
# print(sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3]))

# solution 2
# def sum_ignore_non_numbers(items: list):
#     return sum(item for item in items if isinstance(item, (int, float)))
# print(sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3]))

#task2
# def is_triangle(a, b, c):
#     return a + b > c and a + c > b and b + c > a
#
# # print(is_triangle(2, 4, 9))
#
#task3
# solution1
# import statistics
# def average(*args):
#     return statistics.mean(args) if args else 0
#
# print(average(1,2,3,4,5,6,7,8))
# solution2
# def average(*args):
#     return sum(args)/len(args) if args else 0
#
# print(average(1,2,3,4,5,6,7,8))

task4
def common_strings(list1, list2, ignore_case=True):
    list_common = []
    if ignore_case:
        for string1 in list1:
            if string1.lower() in (" ".join(list2).lower()).split(" "):
                list_common.append(string1.lower())
    else:
        for string1 in list1:
            if string1 in list2:
                list_common.append(string1.lower())

    return list_common

# print(common_strings(["banana", "APPLE", "watermelon", "cherry"], ["Mango", "ApplE", "orange", "cherry"], True))