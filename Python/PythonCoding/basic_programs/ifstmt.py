
#program2
num1 = int(input('Enter a number'))
num2 = int(input('Enter another number'))

if num1 == num2:
    print('Both are equal')
elif num1 > num2:
    print(num1, ' is big')
else:
    print(num2, ' is big')

#Single line comment
""" Doc comment
print ('comment')
"""
''' Multiline comment
print ('comment')
'''

#big3
num1 = int(input('Enter first number'))
num2 = int(input('Enter second number'))
num3 = int(input('Enter third number'))

if num1 == num2 and num2 == num3:
    print('All are equal')
elif num1 > num2 and num1 > num3:
    print('num1 is greater')
elif num2 > num1 and num2 > num3:
    print('num2 is greater')
else:
    print('num3 is greater')

#match case

num = int(input('Enter the day of the week: '))

match num:
    case 1:
        print('Sunday')
    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _:
        print('Not available')
