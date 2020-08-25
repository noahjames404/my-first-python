from RecursionDemo import RecursionDemo
from ManagerEmployee import ManagerEmployee
from Employee import Employee

recursion = RecursionDemo()
recursion.countDown(10)
recursion.countUp(10)

employee = Employee("brandon",21)
manager_employee = ManagerEmployee("noah",21)
manager_employee.promoteEmployee(employee)

wage1 = manager_employee.compute_wage(20,70)
wage2 = employee.compute_wage(30,70)


print(wage1)
print(wage2)
