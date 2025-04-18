#Method is a function associated with a class 
# Class is a blueprint for creating instances
class Employee:
    #Creating a class variable so it can be accessed in any method 
    raise_amount = 1.04
    # class variable to keep track of employee, this shouldn't be easily manipulated
    num_of_emps = 0
    #intializer / constructor
    # self lets us work with all instance e.g 
    # self will pass emp_1 to all class variable
    #init method runs anything we create a new instance 
    def __init__ (self, first, last, pay):
        #set instance variables 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1
    
    #Each method in a class, automatically takes the instance as the 1st arg
    # Don't forget self in method declaration/parameter
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    #A method on applying pay raise 
    def apply_raise(self):
        #You can access class variable using Employee.raise_amount too
        self.pay = int(self.pay * self.raise_amount)

# Unique instances of employee class 
# each instance is a unique employee obj and have diff locations in memory

emp_1 = Employee("olumide", "kolawole", 50000)
emp_2 = Employee("lania", "kolawole", 60000)

# Instance variable contains data unique to each data


print(emp_1.email)
print(emp_2.email)

# Since it's a method it need bracket at the end of it's name
#  so it could return a value to us 
print(emp_2.fullname())

#You can run methods using class name 
# You have to pass the instance as an argument
Employee.fullname(emp_1)