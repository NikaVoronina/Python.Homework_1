# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


x1, y1 = map(int, input('Введите через пробел x1 и y1: ').split())
x2, y2 = map(int, input('Введите через пробел x2 и y2: ').split())
i = round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)
print(i)