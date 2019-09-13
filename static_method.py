
class Employee:

    # static field class field
    minimim_salary = 5000
    def __init__(self, name, salary):
        # instance field
        self.name = name
        self.salary = salary
    # bad idead
    #def upgradeMinimum(self): ...

    # static methods-
    # --------------
    # 1. without self
    # 2. @staticmethod - static + not using static data + not using something specific about this class
    # 3. @classmethod - static + using static data

    # first way - without self
    def getMinimumSalary():
        return Employee.minimim_salary

    # second way - with decorator
    @staticmethod
    def is_working_day(somedate):
        # should not access data
        #return Employee.minimim_salary
        if somedate.weekday() == 4 or somedate.weekday() == 5:
            return False
        return True

    # third way - with decorator
    @classmethod
    def getMinimumSalary(cls):
        return cls.minimim_salary

    @classmethod
    def upgradeMinimumSalary(cls, perc):
        cls.minimim_salary = cls.minimim_salary * perc

    @staticmethod
    def fromstring(emp_string):
        # 'nisim 17000'
        # ['nisim', '17000'] -- split
        e = Employee(emp_string.split()[0],
                     int(emp_string.split()[1]))



print(Employee.minimim_salary)
#Employee.minimim_salary = Employee.minimim_salary * 1.25
Employee.getMinimumSalary()

from datetime import *
my_date = datetime(2019, 9, 11)
print(Employee.is_working_day(my_date))

nisim = Emplopyee('nisim', 17000)

nisim = Employee.fromstring('nisim 17000')
#nisim 17000
#suzi 12374



