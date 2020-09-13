class Employee():
    pay_raise = 0.10

    # def description(self):
    #     print('This is description')
    def __init__(self, first_name, last_name, pay):
        self.fname = first_name
        self.lname = last_name
        self.p = pay
        self.em = self.fname+','+self.lname+'@alabiansolutions.com'
        self.email = self.em.lower()

    def full_name(self):
        return f"{self.fname} {self.lname}"
    
    def salary(self):
        increase = self.pay_raise * self.p
        salary = increase + self.p
        return salary


emp1 = Employee('Michael', 'Uwazie', 2000)
print(f"{emp1.fname}'s pay raise is {emp1.pay_raise}")
print(f"{emp1.fname}'s full name is {emp1.full_name()}")
print(f"{emp1.fname}'s salary is {emp1.salary()}")
print(f"{emp1.fname}'s email is {emp1.email}")


emp2 = Employee('Rote', 'Daniel', 6000)
print(f"{emp2.fname}'s pay raise is {emp2.pay_raise}")
print(f"{emp2.fname}'s full name is {emp2.full_name()}")
print(f"{emp2.fname}'s salary is {emp2.salary()}")
print(f"{emp2.fname}'s email is {emp2.email}")






