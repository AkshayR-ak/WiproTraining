from Day4.bankaccount import BankAccount
from Day4.employee import Employee

print('-----------Bank Account Management System-------------')
Account = BankAccount(206,'Akshay', 25000)
Account.display()
Account.deposit(3000)
Account.withdraw(1000)
Account.display()

print('-----------Employee Management System-------------')
EmployeeHike = Employee(206,'Akshay', 25000)
EmployeeHike.display()
EmployeeHike.salary_hike(20)
EmployeeHike.display()