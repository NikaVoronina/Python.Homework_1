# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
z = int(input('Введите число z: '))

a = x * y * z
b = x + y + z

if a > 0:
    a = 0
if a < 1:
    a = 1
if b > 0:
    b = 1
if b < 1:
    b = 1

leftSide = not (x or y or z)
rightSide = not x and not y and not z
result = leftSide == rightSide

if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')