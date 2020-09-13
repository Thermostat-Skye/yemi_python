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
    


d1 = Developer('Alabi', 'Roben', 3000, "JAVA")
d2 = Developer('Feezat', 'Muyiwa', 3000, "Cpp")
d3 = Developer('Opeolu', 'Ugo', 3000, "Perl")
d4 = Developer('Alanii', 'Chike', 3000, "PHP")


# print(d1.email)
# print(d1.salary())
# d1.details()
# print(d1.prog)

class Manager(Developer):
    def __init__(self, first_name, Last_name, pay, prog_lang, employee):
        super().__init__(first_name, Last_name, pay, prog_lang)
        if employee is not None:
            self.employee = []
        else:
            self.employee = employee 

    def add_emp(self, emp):
        if emp not in self.employee:
            self.employee.append(emp)

    def remove_emp(self, emp):
        if emp in self.employee:
            self.employee.remove(emp)
        
    def list_emp(self):
        for emp in self.employee:
            print(emp.full_name())

m1 = Manager('Bose', 'Lekpa', 6000, 'Mongo', [])

m1.add_emp(d1)
m1.add_emp(d2)
m1.add_emp(d3)
m1.add_emp(d4)
m1.remove_emp(d4)
print(len(m1.employee))
m1.list_emp()

