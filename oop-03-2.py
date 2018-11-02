# Pyhton Object-Oriented Programming
'''
This file shows how to use Static Methods

'''
# Create a class 
class Employee:
    
    # Class Variables
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
    # Instance Variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        
        Employee.num_of_emps += 1
        
    # Regular Methods
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # Class Methods
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    # Class Method as an alt constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    # Static Method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Instance of the Employee Class
emp_1 = Employee('Brian','Lynch',50000 )
emp_2 = Employee('Test','User',60000 )


import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))