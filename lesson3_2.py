# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email,
# телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой


def user_func(name, surename, birthdate, city, email, phone):
    print(f'Имя: {name}, Фамилия: {surename}, Дата рождения: {birthdate}, '
          f'Город проживания: {city}, Эл. почта: {email}, Телефон: {phone}')


user_func(phone='8-800', name='Alex', birthdate='18.06.1956',
          surename='Ivanov', city='Vorkuta', email='alex@gmail.com')
