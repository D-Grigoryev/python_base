# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

def answer(sum_values, mult_values):
    value_1 = 0
    value_2 = 0

    for i in range(sum_values + 1):
        for j in range(mult_values + 1):
            if sum_values == i + j and mult_values == i * j:
                value_1 = i
                value_2 = j
    return value_1, value_2


print(*answer(10, 16))
