#Day 3
import datetime
import math
import os
import random

# Built-in Function
print('-------------Built-in Functions--------------')
# 1 Largest and Smallest
nums = list(map(int, input('Enter the numbers as list: ').split()))
print('Largest number is:', max(nums), 'and Smallest number is ', min(nums), 'in a list')

# 2 Length of String
str1 = str(input("Enter a string to print length: "))
print(len(str1))

# 3 Alphabetical Order
names = input('Enter the names to sort: ').split()
names.sort()
print(names)

# 4 Sum of List
nums = list(map(int, input('Enter the numbers as list to print sum: ').split()))
print(sum(nums))

# 5 Uppercase String
str2 = input('Enter a string to change to uppercase: ')
print(str2.upper())

#User-defined Function
print('-------------User-defined Function--------------')
# 6 Factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

num = int(input('Enter the factorial: '))
print('Factorial is: ',factorial(num))

# 7 Largest of Three
def find_largest(a, b, c):
    return max(a, b, c)

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))
print('Largest number is:', find_largest(a, b, c))

# 8 Greet
def great(name):
    print('Hello', name, '!')

name = input('Enter your name to greet: ')
great(name)

#Built-in and User-Defined functions
print('-------------Built-in and User-Defined functions--------------')
# 9 Average
def average(num):
    return sum(num)/len(num)

avg = list(map(int,input('Enter the numbers to find average: ').split()))
print('Average is:', average(avg))

# 10 Palindrome
def palindrome(str):
    return str[::-1] == str

str = str(input('Enter the string to check palindrome: '))
if palindrome(str):
    print('Palindrome')
else:
    print('Not a Palindrome')

#Math Module
print('-------------Math Module--------------')
# 11 Square root, sine of angle, GCD

num = int(input('Enter the number for square root: '))
print('Square root is: ',math.sqrt(num))

angle = int(input('Enter the number for sine of an angle: '))
print('Sine of an angle is: ',math.sin(angle))

x = int(input('Enter the first number to find GCD: '))
y = int(input('Enter the second number to find GCD: '))
print('GCD is', math.gcd(x,y))

# 12 Random Module
print('-------------Random Module--------------')
print("Random Integer:", random.randint(1, 100))

list = [random.randint(1, 50) for i in range(5)]
print("Random List:", list)

list = [1, 2, 3, 4, 5]
random.shuffle(list)
print("Shuffled List:", list)

# 13 Datetime Module
print('-------------Datetime Module--------------')
now = datetime.datetime.now()
print("Current Date and Time:", now)

date1 = datetime.date(2004, 4, 1)
date2 = datetime.date(2026, 4, 25)
diff = date2 - date1
print("Days Between Dates:", diff.days)

print("Date Format:", now.strftime("%d-%m-%Y"))

# 14 OS Module
print('-------------OS Module--------------')
print("Current Working Directory:", os.getcwd())

folder = "Day3"

if not os.path.exists(folder):
    os.mkdir(folder)

print("If Directory Exists:", os.path.exists(folder))

print("Files and Folders:")
print(os.listdir())