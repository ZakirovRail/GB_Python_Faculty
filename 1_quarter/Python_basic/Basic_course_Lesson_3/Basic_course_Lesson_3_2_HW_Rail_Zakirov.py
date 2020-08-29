"""
2)	Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


# def user_data(name, surname, birth_year, city_living, email, phone):
#     print(f'The user {name} {surname} was born in {birth_year} year, lives in {city_living} city. '
#           f'Contacts: email - {email} and phone number - {phone} ')
#
#
# user_data(name='Mike', surname='Suvorov', birth_year='1985', city_living='Mexico', email='test@gmail.com',
#           phone='+11534225665')


#Solution from teacher
def personal_info(**kwargs):
    return kwargs


print(personal_info(
    name=input('Name: '),
    surname=input('Surname: '),
    birthday=input('BD: '),
    city=input('City: '),
    email=input('Email: '),
    phone=input('Phone number: ')
))

personal_info(name='Mike', surname='Suvorov', birth_year='1985', city_living='Mexico', email='test@gmail.com',
          phone='+11534225665')

