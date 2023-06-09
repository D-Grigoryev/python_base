# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый,
# т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

#Решение - 1 с математическими операциями
def happy(number=input('Введите шестизначное число: ')):
    a = int(number)
    sum_el_1 = 0
    sum_el_2 = 0
    for i in range(len(number)):
        if i < 3:
            sum_el_1 += a % 10
        else:
            sum_el_2 += a % 10
        a = a // 10
    if sum_el_1 == sum_el_2:
        return 'Yes'
    return 'No'

#Решение - 2 без математических операций
def happy_1(number=input('Введите шестизначное число: ')):
    if (int(number[0]) + int(number[1]) + int(number[2])) == (int(number[3]) + int(number[4]) + int(number[5])):
        return 'Yes'
    return 'No'


print(happy())
print(happy_1())
