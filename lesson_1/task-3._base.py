"""x
Задание 3.
Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
Пример:
Введите число n: 3
n + nn + nnn = 369
"""
num = input('Введите целое положительное число: ')
print(f'Сумма чисел {num} + {num + num} + {num + num + num} = {int(num) + int(num * 2) + int(num * 3)} ')
