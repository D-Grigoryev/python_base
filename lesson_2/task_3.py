# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def func(n):
    i = 0
    while 2 ** i <= n:
        print(2 ** i)
        i += 1

func(100)