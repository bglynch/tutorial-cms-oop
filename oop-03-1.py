# Pyhton Object-Oriented Programming
'''
This file shows how to use Class Methods
1. Create a classmethod to so that we can alter the raise amount

2. Example where we are given employee data in a hyphen seperated string
   We use a Class Method as an Alt cConstructor to parse the string and create an Employee Instance
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

# Instance of the Employee Class
emp_1 = Employee('Brian','Lynch',50000 )
emp_2 = Employee('Test','User',60000 )

# 
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
