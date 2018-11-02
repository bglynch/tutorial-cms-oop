# Pyhton Object-Oriented Programming
'''
This file show the ability to update a Class Variable for either:
    1. The Class
    2. An Individual instance
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
        
    # Class Methods
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Instance of the Employee Class
emp_1 = Employee('Brian','Lynch',50000 )
emp_2 = Employee('Test','User',60000 )

print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Update the Class Variable
Employee.raise_amount = 1.05
print(' ')
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Update an Class Variable for an Individual Instance of a Class
print(' ')
print(emp_1.__dict__)

emp_1.raise_amount = 1.06

print(emp_1.__dict__)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
