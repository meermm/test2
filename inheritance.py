'''
Наследование позволяет нам определить класс, который наследует все методы и свойства из родительского класса, а также позволяет нам добавлять больше функциональности. Дочерний класс - это класс, наследуемый от родительского класса,

'''

class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age  

 
class Employee(Person):       # наследуется от класса Person
    def details(self, company):
        print(self.name, "работает в компании", company + ".", "Ему", self.age, "лет.")

 
tom = Employee("Tom", 25)
tom.details("Google")
