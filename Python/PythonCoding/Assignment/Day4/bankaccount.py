class BankAccount:

    def __init__(self, acc_no, holder_name, balance):
        self.__account_number = acc_no
        self.__account_holder = holder_name
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    def set_account_number(self, acc_no):
        self.__account_number = acc_no

    def set_account_holder(self, holder_name):
        self.__account_holder = holder_name

    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(amount, 'deposited successfully')

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(amount, 'withdrawn successfully')
        else:
            print('Insufficient Balance')

    def display(self):
        print('Bank Account Details')
        print('Account Number:', self.__account_number)
        print('Account Holder:', self.__account_holder)
        print('Balance:', self.__balance)