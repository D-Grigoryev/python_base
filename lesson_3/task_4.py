# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()
# """

# Решение с использованием функции sort()
def my_func(a, b, c):
    list_1 = [a, b, c]
    list_1.sort()
    return list_1[-1] + list_1[-2]


# Решение без использования функции sort()
def my_func_diff(a, b, c):
    list_1 = [a, b, c]
    for i in range(len(list_1) - 1, 0, -1):
        for j in range(i):
            if list_1[j] > list_1[j + 1]:
                list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]
    return list_1[-1] + list_1[-2]


print(my_func(3, 12, 7))
print(my_func_diff(3, 12, 7))
