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

# HOW TO MODUFY THE METHOD DEFINE ONE THE PARENT CLASS
class Developer(Employee):
    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog = prog_lang


  
    def details(self):
        print('Here is your full details')
        print(F'{self.fname} {self.lname} {self.email} {self.salary()}')
    


d1 = Developer('Alabi', 'Paul', 3000, "JAVA")

print(d1.email)
print(d1.salary())
d1.details()
print(d1.prog)






