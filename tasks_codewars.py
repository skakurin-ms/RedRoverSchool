# import re
#
#
# def find_hack(arr):
scores = {
    "A": 30,
    "B": 20,
    "C": 10,
    "D": 5
}
#     result_names = []
#     print(len(array))
#     for arr in range(len(array)):
#         total_points = (array[arr][2].count("A") * scores["A"] + array[arr][2].count("B") * scores["B"] + array[arr][2].count("C") * scores["C"] + array[arr][2].count("D") * scores["D"])
#         if len(array[arr][2]) >= 5 and "C" not in array[arr][2] and "D" not in array[arr][2]:
#             total_points += 20
#         if array[arr][1] != min(total_points, 200) or array[arr][1] > 200 or re.search(r"[E-Z]", "".join(array[arr][2])):
#             result_names.append(array[arr][0])
#     return result_names
#
array = [
  ["name1", 445, ["B", "A", "A", "C", "A", "A"]],     # name1 total point is over 200 => hacked
  ["name2", 160, ["B", "A", "A", "A", "A"]],               # name2 point is right
  ["name3", 200, ["B", "A", "A", "C"]],               # name3 point is 200 but real point is 90 => hacked
  ["name4", 200, ["A", "A", "A", "A", "A", "A", "A"]] # name4 point is right
]
#
# print(find_hack(array))

point = lambda arrays, scoress: [sum(scoress[arrays[i][2]]) for i in arrays]
print(point(array,scores))
