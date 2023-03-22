# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*
#
# ноутбук
#     12

list_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']  # -1 point
list_2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']  # -2 point
list_3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']  # -3 point
list_4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']  # –4 очка;
list_5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']  # -5 очков;
list_6 = ['J', 'X', 'Ш', 'Э', 'Ю']  # –8 очков;
list_7 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']  # –10 очков.


def score(user_word):
    summ_elements = 0
    for el in user_word:
        summ_elements += list_1.count(el)
    for el in user_word:
        summ_elements += 2 if list_2.count(el) > 0 else 0
    for el in user_word:
        summ_elements += 3 if list_3.count(el) > 0 else 0
    for el in user_word:
        summ_elements += 4 if list_4.count(el) > 0 else 0
    for el in user_word:
        summ_elements += 5 if list_5.count(el) > 0 else 0
    for el in user_word:
        summ_elements += 8 if list_6.count(el) > 0 else 0
    for el in user_word:
        summ_elements += 10 if list_7.count(el) > 0 else 0
    return summ_elements


print(score('ноутбук'.upper()))
