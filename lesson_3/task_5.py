# ДОПОЛНИТЕЛЬНЫЕ ЗАДАНИЯ:
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1

def find_x(user_number=int(input('Введите число: ')), x=int(input('Введите Х: '))):
    list_numbers = []
    for i in range(user_number):
        list_numbers.append(i + 1)
    print(list_numbers)
    print(x)
    return list_numbers.count(x)


print(find_x())
