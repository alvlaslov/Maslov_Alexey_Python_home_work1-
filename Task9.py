# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = input('Input number of quarter from 1 to 4: ')
count = 0
while count == 0:
    if quarter.isdigit() == True and int(quarter) <= 4 and int(quarter) >= 1:
        if int(quarter) == 1:
            print(f'The range of possible coordinates of points: x > 0, y > 0')
        elif int(quarter) == 2:
            print(f'The range of possible coordinates of points: x < 0, y > 0')
        elif int(quarter) == 3:
            print(f'The range of possible coordinates of points: x < 0, y < 0') 
        else:
            print(f'The range of possible coordinates of points: x > 0, y < 0') 
        count+=1
    else:
         print(f'You entered not a number or wrong number')
         quarter = input('Input number of quarter from 1 to 4: ')

