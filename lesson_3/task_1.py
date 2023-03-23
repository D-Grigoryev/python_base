# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень

dict_1 = {'зима': (1, 2, 12), 'весна': (3, 4, 5), 'лето': (6, 7, 8), 'осень': (9, 10, 11)}
list_1 = ['зима', 'весна', 'лето', 'осень']


# Вариант решения с использованием dict
def seasons_dict(number, dic):
    return [k for (k, n) in dic.items() if number in n]


# Вариант решения с использованием list
def seasons_list(number, lis):
    if 3 <= number < 6:
        return lis[1]
    if 6 <= number < 9:
        return lis[2]
    if 9 <= number < 12:
        return lis[3]
    if 1 <= number < 3 or number == 12:
        return lis[0]
    return 'Введено неверное значение'


print(*seasons_dict(5, dict_1))
print(seasons_list(13, list_1))
