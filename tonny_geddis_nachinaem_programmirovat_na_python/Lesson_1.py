# 1.	Персональные данные. Напишите программу, которая выводит приведенную ниже информацию:
# •	ваше имя;
# •	ваш адрес проживания, с городом, областью и почтовым индексом;
# •	ваш номер телефона;
# •	вашу специализацию в учебном заведении.

first_name = 'Егор'
last_name = 'Наумов'

city = 'Пермь'
region = 'Пермский край'
postal_code = 614095

phone = 89194862952

specialization = 'кодер'

print('Моё имя:', first_name)


join_name = ' '.join(['Моё полное имя:', last_name, first_name])
print(join_name)
print('Моё полное имя:', end=' ')
print(last_name, end=' ')
print(first_name)
print()

full_name = last_name + ' ' + first_name
print('Моё полное имя:', full_name)

print('Адрес проживания:', end=" ")
print(postal_code, region, 'г. '+city, sep=', ', end='\n\n')

print('Телефон:', phone)

print('\n', 'Я - ', specialization, sep='')

print()

print(f'Я - {specialization}')