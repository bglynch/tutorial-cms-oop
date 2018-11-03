# Pyhton Object-Oriented Programming
'''
This file shows Class Inheritance
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

# Create a Subclass that inherits from Employee
class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        # super().__init__(first, last, pay)
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        # super().__init__(first, last, pay)
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->'+emp.fullname())


# Instance of the Employee Class
emp_1 = Employee('Average','Joe',40000 )
dev_1 = Developer('Brian','Lynch',50000, 'Python' )
dev_2 = Developer('Test','User',60000 ,'Java')

mgr_1 = Manager('Sue','Smith',90000, [dev_1])

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print('')
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
