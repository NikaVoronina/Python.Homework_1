# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

a = int(input('Введите a: '))
b = int(input('Введите b: '))
if a * a == b:
    print('Да')
else:
    print('Нет')

# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90