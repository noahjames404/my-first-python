class Employee:

    #the self paremeter is a reference
    #to the current instance of the class - w3schools/python
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def compute_wage(self,hours, rate):
        return hours * rate
