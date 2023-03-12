# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
import random


def coins(n=int(input("Введите число монет лежащих на столе: "))):
    eagle_value = 0
    tails_value = 0
    while n > 0:
        coin_value = random.randint(0, 1)
        print(f'{coin_value}')
        if coin_value > 0:
            eagle_value += 1
        else:
            tails_value += 1
        n -= 1
    return f'Необходимо переверуть {eagle_value} монеток со значнием Орел' if eagle_value < tails_value \
        else f'Необходимо переверуть {tails_value} монеток со значеним Решка'


print(coins())
