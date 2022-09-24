# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# First method

# list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# number = int(input('Input a number from 1 to 7 corresponding to the day of the week: '))
# if 1<=number<=5:
#     print(f'The number "{number}" corresponds to {list[number - 1]}. {list[number - 1]} is a work day.')
# elif 6<=number<=7:
#     print(f'The number "{number}" corresponds to {list[number - 1]}. {list[number - 1]} is a day off.')
# else:
#     print(f'The number "{number}" does not match the condition. Please, repeat the input.')

# Second method

list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
number = input('Input a number from 1 to 7 corresponding to the day of the week: ')
count = 0
while count == 0:
    if number.isdigit() == True and int(number) <= 7 and not int(number) <= 0:
        if int(number) < 6:
            print(f'The number "{number}" corresponds to {list[int(number) - 1]}. {list[int(number) - 1]} is a work day.')
        else:
            print(f'The number "{number}" corresponds to {list[int(number) - 1]}. {list[int(number) - 1]} is a day off.')
        count += 1
    else:
        print(f'You entered not a number or wrong number')
        number = input('Input a number from 1 to 7 corresponding to the day of the week: ')
