# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# Решение-1 без использования математичского подхода
def sum_elements(number=input('Введите трехзначное число: ')):
    return int(number[0]) + int(number[1]) + int(number[2])


# Решение-2 с использование математического подхода
def sum_elements_2(number=input('Введите трехзначное число: ')):
    a = int(number)
    sum_el = 0
    for i in range(len(number)):
        sum_el += a % 10
        a = a // 10
    return sum_el


print(sum_elements())
print(sum_elements_2())
