'''
Полиморфизм означает, что одно и то же имя функции (но разные сигнатуры) используется для разных типов.
А также в Python полиморфизм позволяет нам определять методы в дочернем классе, которые имеют то же имя, что и методы в родительском классе. При наследовании дочерний класс наследует методы от родительского класса. Однако можно изменить метод в дочернем классе, который он унаследовал от родительского класса.
'''

# Пример встроенных полиморфных функций:
  
# len () используется для строки
print(len("geeks"))
  
# len () используется для массива
print(len([10, 20, 30]))


# Примеры используемых определенных полиморфных функций:

def add(x, y, z = 0): 
    return x + y + z
  
print(add(2, 3))
print(add(2, 3, 4))

# В приведенном ниже коде показано, как Python может одинаково использовать два разных типа классов.
class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington is the capital of USA.")

	def language(self):
		print("English is the language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()
