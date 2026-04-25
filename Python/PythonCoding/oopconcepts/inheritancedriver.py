from oopconcepts.college import College
from oopconcepts.student import Student
from oopconcepts.studentgrade import StudentGrade
from oopconcepts.teacher import Teacher

cname = input('Enter the College name: ')
ccode = int(input('Enter the College code: '))
ccity = input('Enter the College city: ')
rollno = int(input('Enter the your Rollno: '))
sname = input('Enter the your Student name: ')
mark1 = int(input('Enter the Mark1: '))
mark2 = int(input('Enter the Mark2: '))
mark3 = int(input('Enter the Mark3: '))
eid = int(input('Emp id: '))
tn = input('Teacher name: ')
de = input('Enter department: ')
bp = int(input('Enter Basic pay: '))

project = College(cname, ccode, ccity)
project.welcome_message()
project.display_college_details()

project = Student(cname, ccode, ccity, rollno, sname, mark1, mark2, mark3)
print('Total is: ', project.calculate_total())
print('Average is: ', project.calculate_average())

project = StudentGrade(cname, ccode, ccity, rollno, sname, mark1, mark2, mark3)
project.calculate_result()
project.calculate_grade()
print(f'Result: {project.result} \t Grade: {project.grade}')

teach = Teacher(ccode, cname, ccity, eid, tn, de, bp)
print(f'Eid: {teach.empid} \t Name: {teach.tname} \t Dept: {teach.dept}')
print(f'Salary: {teach.calculate_salary()}')

