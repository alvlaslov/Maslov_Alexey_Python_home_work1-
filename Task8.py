# Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У 

x = int(input('Input a coordinate X: '))
y = int(input('Input a coordinate Y: '))
if x == 0 and y == 0:
    print(f'The point with coordinates ({x}, {y}) is the center coordinates.')
elif x == 0 and (y > 0 or y < 0):
    print(f'The point with coordinates ({x}, {y}) lies on the "y" axis.')
elif (x > 0 or x < 0) and y == 0:
    print(f'The point with coordinates ({x}, {y}) lies on the "x" axis.')
elif x > 0 and y > 0:
    print(f'The point with coordinates ({x}, {y}) is located in the first coordinate quarter.')
elif x < 0 and y > 0:
    print(f'The point with coordinates ({x}, {y}) is located in the second coordinate quarter.')
elif x < 0 and y < 0:
    print(f'The point with coordinates ({x}, {y}) is located in the third coordinate quarter.')
else:
    print(f'The point with coordinates ({x}, {y}) is located in the fourth coordinate quarter.')