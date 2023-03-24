# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
import random

user_number_one = int(input('Введите количество элементов 1-го массива: '))
user_number_two = int(input('Введите количество элементов второго массива: '))


def creat_uniq_arr(first, second):
    first_numbers = {random.randint(0, first) for i in range(first)}
    second_numbers = {random.randint(0, second) for i in range(second)}
    print(f' Первый массив - {first_numbers} \n Второй массив - {second_numbers} \n Уникальные элементы - '
          f'{first_numbers.intersection(second_numbers)}')


creat_uniq_arr(user_number_one, user_number_two)
