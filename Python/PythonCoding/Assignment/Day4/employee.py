class Employee:

    def __init__(self, emp_id, name, salary):
        self.__employee_id = emp_id
        self.__name = name
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_employee_id(self, emp_id):
        self.__employee_id = emp_id

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print('Employee Details')
        print('Employee ID:', self.__employee_id)
        print('Name:', self.__name)
        print('Salary:', self.__salary)

    def salary_hike(self, percent):
        increase = self.__salary * percent / 100
        self.__salary += increase
        print(percent, '% salary hike applied')