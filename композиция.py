'''
По композиции один из классов состоит из одного или нескольких экземпляров других классов.
Другими словами, один класс является контейнером, а другой класс - содержимым, и если вы удалите объект-контейнер, все его объекты содержимого также будут удалены.

'''

class Salary:
    def __init__(self, pay):
        self.pay = pay
 
    def get_total(self):
        return (self.pay*12)
 
 
class Human:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay)
 
    def annual_salary(self):
        return "Total: " + str(self.obj_salary.get_total() + self.bonus)
 
 
obj_emp = Human(680, 500)
print(obj_emp.annual_salary())