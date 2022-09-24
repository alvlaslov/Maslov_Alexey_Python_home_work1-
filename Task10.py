# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

ax = int(input('Input "X" for "A": '))
ay = int(input('Input "Y" for "A": '))
bx = int(input('Input "X" for "B": '))
by = int(input('Input "Y" for "B": '))
length = ((bx - ax)**2 + (by - ay)**2)**(1/2)
print(round(length, 3))
