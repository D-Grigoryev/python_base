# 3. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
# Пример:
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456
# """
# """


def personal_info(name='Иван', surname='Иванов', year_of_b=1846,
                  residence='Москва', e_mail='jackie@gmail.com', phone='01005321456'):
    print(
        f'{name} {surname} {year_of_b} года рождения, проживает в городе {residence}, '
        f'email: {e_mail}, телефон: {phone}')


personal_info()