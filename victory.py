#Написать или улучшить программу Викторина из предыдущего дз
# (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
#Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') -
# предлагаю для тренировки пока использовать строку

import random
freend_1 = {
    'name': 'Alex',
    'date': '01.01.1987',
    'full_date': 'Первое января 1987 года',
}
freend_2 = {
    'name': 'Oleg',
    'date': '01.02.1988',
    'full_date': 'Первое февраля 1988 года',
}
freend_3 = {
    'name': 'Vova',
    'date': '01.03.1989',
    'full_date': 'Первое марта 1989 года',
}
freend_4 = {
    'name': 'Egor',
    'date': '01.04.1990',
    'full_date': 'Первое апреля 1990 года',
}
freend_5 = {
    'name': 'Dima',
    'date': '01.05.1991',
    'full_date': 'Первое мая 1991 года',
}
freend_6 = {
    'name': 'lena',
    'date': '01.06.2000',
    'full_date': 'Первое июня 2000 года',
}
freend_7 = {
    'name': 'Tihan',
    'date': '01.07.2001',
    'full_date': 'Первое июля 2001 года',
}
freend_8 = {
    'name': 'Max',
    'date': '01.08.2002',
    'full_date': 'Первое августа 2002 года',
}
freend_9 = {
    'name': 'Fedor',
    'date': '01.09.2003',
    'full_date': 'Первое сентября 2003 года',
}
freend_10 = {
    'name': 'Ivan',
    'date': '01.10.2004',
    'full_date': 'Первое октября 2004 года',
}
#Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random
freend_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = random.sample(freend_number, 5)
#print(result)

#После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
print('Введите дату в формате ДД.ММ.ГГГГ ')

victory = 0
for i in result:
    #print(i)
    if i == 1:
        date = input('Дата рождения Alex :')
        if date in freend_1['date']:
            victory += 1
        else:
            print('Правильны ответ : ', freend_1['full_date'])
# Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ,
# но уже в следующем виде:
# третье января 2009 года, склонением можно пренебречь
    if i == 2:
        date = input('Дата рождения Oleg :')
        if date in freend_2['date']:
            victory += 1
        else:
            print('Правильны ответ : ', freend_2['full_date'])
    if i == 3:
        date = input('Дата рождения Vova :')
        if date in freend_3['date']:
            victory += 1
        else:
            print('Правильны ответ : ', freend_3['full_date'])
    if i == 4:
        date = input('Дата рождения Egor :')
        if date in freend_4['date']:
            victory += 1
        else:
            print('Правильны ответ : ', freend_4['full_date'])
    if i == 5:
        date = input('Дата рождения Dima :')
        if date in freend_5['date']:
            victory += 1
        else:
            print('Правильны ответ : ', freend_5['full_date'])
    if i == 6:
        date = input('Дата рождения lena :')
        if date in freend_6['date']:
            victory += 1
        else:
            print('Правильны ответ : ', freend_6['full_date'])
    if i == 7:
        date = input('Дата рождения Tihan :')
        if date in freend_7['date']:
            victory += 1
        else:
            print('Правильны ответ : ', freend_7['full_date'])
    if i == 8:
        date = input('Дата рождения Max :')
        if date in freend_8['date']:
            victory += 1
        else:
            print('Правильны ответ : ', freend_8['full_date'])
    if i == 9:
        date = input('Дата рождения Fedor :')
        if date in freend_9['date']:
            victory += 1
        else:
            print('Правильны ответ : ', freend_9['full_date'])
    if i == 10:
        date = input('Дата рождения Ivan :')
        if date in freend_10['date']:
            victory += 1
        else:
            print('Правильны ответ : ', freend_10['full_date'])
#В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
print('Количество правильных ответов = ', victory)
print('Количество НЕ правильных ответов = ', 5 - victory)



