from Employee import Employee

class ManagerEmployee(Employee):

    def __init__(self,name,age):
        Employee.__init__(self,name,age)

    def promoteEmployee(self,employee):
        print(employee.name + " is promoted!")
