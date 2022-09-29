# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

num = int(input('Введите число: '))
num_result = (num % 5 == 0 or num % 10 ==0 or num % 15 == 0) and not num % 30 == 0
print(num, num_result, sep = " -> ")