# Pyhton Object-Oriented Programming
'''
This file shows Special Methods we can use in Classes
Thses are also know as Magic Methods
'''
# Create a class 
class Employee:
    
    # Class Variables
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
    # Instance Variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        
        
    # Regular Methods
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
        
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)
        
    def __add__(self, other):
        return self.pay + other.pay
        
    def __len__(self):
        return len(self.fullname())


# Instance of the Employee Class
emp_1 = Employee('Average','Joe',40000 )
emp_2 = Employee('Brian','Lynch',60000 )

print(len(emp_1))

print(len('test'))
print('test'.__len__())