#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

# TODO здесь ваш код
s=my_favorite_movies
x=s.find(',')
print(s[:x])
y=s.rfind(',')
print(s[y+2:])
s1=s[x+2:y]
x=s1.find(',')
print(s1[:x])
y=s1.rfind(',')
print(s1[y+2:])