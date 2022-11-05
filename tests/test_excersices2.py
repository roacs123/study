class Employee():
	"""Класс представляет работника"""
	def __init__(self, first_name, last_name, year_salary):
		"""Метод инициирует данные работника"""
		self.first_name = first_name
		self.last_name = last_name
		self.year_salary = year_salary
	
	def give_raise(self, up_sal=5000):
		"""Увеличивает зарплату на 5000$"""
		self.year_salary += up_sal
		
	def show_salary(self):
		"""Показывает текущую зарплату"""
		print(f"{self.first_name.title()} {self.last_name.title()} получает зарплату {str(self.year_salary)}")
		
admin = Employee('вася', 'пупкин', 1000)
admin.show_salary()
admin.give_raise(1000)
admin.show_salary()
