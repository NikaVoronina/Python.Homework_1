# print("hello, world")

# типы переменных:
# int, float, boolean, str, list, None


# value = None
# print(type(value))

# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))
# s = "hello 'world'"

# print(s) # вывод строки

# print(a, '-', b, '-', s)
# print('{1} - {2} - {0}'.format(a, b, s))
# print(f'{a} - {b} - {s}')

# f = True
# print(f)
# list = ['1', '2', '3', 'hello']
# col = ['hello', 1, 2, 4, 5, True]
# print(list)
# print(col)

# print() - отвечает за вывод данных
# input() - отвечает за ввод данных

# print('Введите a: ')
# a = int(input())
# print('Введите b: ')
# b = int(input())
# print(a, '+', b, '=', a + b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# print('Введите a: ')
# a = float(input())
# print('Введите b: ')
# b = float(input())
# print(a, '+', b, '=', a + b)

# // - деление без остатка (целое число по итогу)
# % - остаток от деления
# ** - возведение в степень
# round - округление по математическим правилам
# a = 1.3
# b = 3
# c = round(a * b, 3) # округление до трёх чисел
# print(c)

# a = 3
# a += 5 # a = a + 5

# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# a = 1 < 3 and 5 > 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1, 2]
# b = [1, 2]
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 123
# print(func < T > (x))

# f = 1 > 2 or 4 < 6 # будет True, потому что хотя бы одно из высказываний истинно
# print(f)

# f = [1, 2, 3, 4]
# print(f)
# print(5 in f)

# is_odd = not f[0] % 2
# print(is_odd)


# if condition:
    # operator 1
    # operator 2
    # . . .
    # operator n
# else:
    # operator n + 1
    # operator n + 2
    # . . .
    # operator n + m

# username = input('Введите имя: ')
# if(username == 'Маша'):
#     print('Ура, это же МАША!')
# else:
#     print('Привет,', username)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# if comdition1:
    # operator
# elif condition2:
    # operator
# elif condition3:
    # operator
# else:
    # operator

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет,', username)

# Цикл позволяет выполнить блок операторов какое-то количество раз:
# while condition:
    # operator 1
    # operator 2
    # . . .
    # operator n

# original = 23
# inverted = 0
# while original != 0: # не равен 0
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# while condition:
    # operator 1
    # operator 2
    # . . .
    # operator n
# else:
    # operator n + 1
    # operator n + 2
    # . . .
    # operator n + m

# original = 23
# inverted = 0
# while original != 0: # не равен 0
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original) # увидеть каждый этап
# else:
#     print('Пожалуй,')
#     print('хватит')
# print(inverted)

# for i in enumeration:
    # operator 1
    # operator 2
    # . . .
    # operator n

# list = 1, 2, 3, 4, 5
# for i in list:
#     print(i ** 2)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(1, 5):
#     print(i)

# for i in range(1, 10, 2): # через две цифры
#     print(i)

# text = 'съешь этих мягких французских булок'
# print(len(text))            # 39
# print('ещё' in text)           # True
# print(text.isdigit())       # False
# print(text.islower())       # True
# print(text.replase('ещё', 'ЕЩЁ')) #

# for c in text:
    # print(c)

# СПИСКИ

# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]

# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]

# for i in numbers:
#     i *= 2
#     print(i)    # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]

# ФУНКЦИИ

# def function_name(x):
    # body line 1
    # . . .
    # body line n
    # optional return

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

arg = 2.3
print(f(arg))
print(type(f(arg)))