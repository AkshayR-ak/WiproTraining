#Day 1

# 1 Voting Eligibility
print('--------1 Voting Eligibility----------')
age = int(input("Enter your age to check Voting Eligibility: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 2 Leap Year
print('--------2 Leap Year----------')
year = int(input("Enter a year to check Leap year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 3 Divisible by 5
print('--------3 Divisible by 5----------')
num = int(input("Enter a number to check divisible by 5: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# 4 Vowel or Consonant
print('--------4 Vowel or Consonant----------')
ch = input("Enter a character to check Vowel or Consonant: ").lower()
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# 5 Strong Password
print('--------5 Strong Password----------')
password = input("Enter password to check strong or weak: ")
if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")

# 6 Grade using match-case
print('--------6 Grade using match-case----------')
grade = input("Enter grade to check using Match-case: ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "D":
        print("Poor")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")

# 7 Traffic Light
print('--------7 Traffic Light----------')
color = input("Enter traffic light color to check using Match-case: ").capitalize()

match color:
    case "Red":
        print("Stop")
    case "Yellow":
        print("Wait")
    case "Green":
        print("Go")
    case _:
        print("Invalid Color")

# 8 Factorial using for loop
print('--------8 Factorial using for loop----------')
n = int(input("Enter a number to calculate factorial using for loop: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)

# 9 Even numbers 1 to 20
print('--------9 Even numbers 1 to 20----------')
print("Even a numbers to print even numbers using for loop:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 10 Countdown timer
print('--------10 Countdown timer----------')
print('Printing countdown timer from 10 to 0')
count = 10
while count >= 0:
    print(count)
    count -= 1

# 11 Count vowels in string
print('--------11 Count vowels in string----------')
text = input("Enter string to count vowels: ").lower()
vowels = 0

for i in text:
    if i in "aeiou":
        vowels += 1

print("Vowel Count:", vowels)

# 12 Continue and Break
print('--------12 Continue and Break----------')
print('Printing 1 to 10 to check continue and break: ')
for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)