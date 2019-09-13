
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
    # 2. @staticmethod - static +
    #     + not using static data + not specific related
    #       to this class
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


    @classmethod
    def fromstring(cls, emp_string):
        # 'nisim 17000'
        # ['nisim', '17000'] -- split
        e = Employee(emp_string.split()[0],
                     int(emp_string.split()[1]))

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

# tagil:
# write Mobile class
# __init__(self, color, price, heat)
# static/class data -
#    model_name - choose whatever you want...
#    max_heat
# static/class methods:
#   getmaxheat() - write in 3 ways
#   getmodelname() - write as @classmethod
#   updatemaxheat(newmaxheat) - write as @classmethod
#   fromstring('color#price#heat' - dont forget casting
#   fromlist(['color', price, heat]
#   getvendor - write as @staticmethod,
#       returns 'android' or 'iphone'


