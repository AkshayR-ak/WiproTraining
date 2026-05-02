#Day 5

#1. Write in a file
print('1. Write in a file')
text = input('Enter text to save in a file:')
filename = 'output.txt'
with open(filename, 'w') as file:
    file.write(text)

with open(filename, 'r') as file:
    print('Output:')
    print(file.read())

#2. Read in a file
print('2. Read in a file')
with open("sample.txt", "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)

#3. Copy a file
print('3. Copy a file')
with open('source.txt', 'r') as file:
    content = file.read()

with open('destination.txt', 'w') as file:
    file.write(content)

with open('destination.txt', 'r') as file:
    print(file.read())

#4. Append a file
print('4. Append a file')
content = 'Appended Successfully.'
with open('log.txt', 'a') as file:
    file.write(content)

with open('log.txt', 'r') as file:
    print(file.read())

#5. Exception Handling: String to int
print('5. Exception Handling: String to int')
try:
    num = int(input('Enter a number:'))
    print('Integer value:', num)
except ValueError:
    print('Invalid input')

#6. Exception Handling: File exist or not
print('6. Exception Handling: File exist or not')
filename = input('Enter filename:')
try:
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print('File not found.')

#7. Exception Handling: ZeroDivisionError & ValueError
print('7. Exception Handling: ZeroDivisionError & ValueError')
try:
    a= float(input('Enter a number A:'))
    b = float(input('Enter a number B:'))
    result = a / b
    print(result)
except ZeroDivisionError:
    print('Cannot divide by zero')
except ValueError:
    print('Invalid input')

#8. Exception Handling: IndexError
print('8. Exception Handling: IndexError')
try:
    listnum = [1,2,3,4,5]
    num = int(input('Enter a index to access in list:'))
    print(listnum[num])
except IndexError:
    print('Index out of range')

#9. Custom Exception: NegativeNumberError
print('9. Custom Exception: NegativeNumberError')
class NegativeNumberError(Exception):
    pass

try:
    num = int(input('Enter a positive number:'))
    if num < 0:
        raise NegativeNumberError("Negative number entered.")
    print("Valid number:", num)
except NegativeNumberError as err:
    print(err)

#10. Exception Handling: loop
print('10. Exception Handling: loop')
while True:
    try:
        num1 = int(input('Enter a num1:'))
        num2 = int(input('Enter a num2:'))
        res = num1 / num2
        print(res)
        break
    except ZeroDivisionError:
        print('Cannot divide by zero')
    except ValueError:
        print('Invalid input')

#11. try-except-finally block
print('11. try-except-finally block')
try:
    with open('hi.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('File not found.')
finally:
    print('Finally printed')

#12. Exception Handling: Function
print('12. Exception Handling: Function')
def add(num1, num2):
    try:
        return num1 + num2
    except TypeError:
        print('Invalid input')

num1 = int(input('Enter num1:'))
num2 = int(input('Enter num2:'))
print(add(num1, num2))

#13. Exception Handling: ValueError
print('13. Exception Handling: ValueError')
while True:
    try:
        num = int(input('Enter a num:'))
        print(num)
        break
    except ValueError:
        print('Invalid input')
