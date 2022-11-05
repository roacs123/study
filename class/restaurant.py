class Restaurant():
	"""Модель ресторана"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Инициализирует атрибуты название ресторана и тип кухни"""
		self.r_name = restaurant_name
		self.c_type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		"""Описывает ресторан"""
		print(f"Название ресторана {self.r_name.title()}, а кухня там {self.c_type}.")
	
	def open_restaurant(self):
		"""Открытие ресторана"""
		print(f"Ресторан {self.r_name.title()} открыт!")
	
	def count_number_served(self):
		"""Выдаёт отформатированное количество посетителей"""
		print(f"Количество посетителей ресторана сегодня: {str(self.number_served)}.")
	
	def set_numver_served(self, number):
		"""Задаёт количество посетителей"""
		self.number_served = number
	
	def increment_number_served(self, inc_number):
		"""Добавляет количество посетителей в атрибут"""
		if inc_number > 0:
			self.number_served += inc_number
		else:
			print("Нельзя использовать отрицательное значение количества посетителей!")

class User():
	"""Профиль пользователя"""
	def __init__(self, first_name, last_name, age, country):
		"""Инициализирует данные пользователя"""
		self.f_name = first_name
		self.l_name = last_name
		self.full_name = first_name + ' ' + last_name
		self.age = age
		self.country = country
		self.login_attempts = 0
		
	def describe_user(self):
		"""Описывает пользователя"""
		print(f"Пользователь {self.full_name.title()} проживает в городе {self.country.title()} и его возраст {str(self.age)}.")
	
	def greet_user(self):
		"""Приветствует пользователя"""
		print(f"Привет, {self.f_name.title()}!")
		
	def increament_login_attempts(self):
		"""Увеличивает количество попыток логина на 1"""
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		"""Обнуляет количество попыток логина"""
		self.login_attempts = 0
		

