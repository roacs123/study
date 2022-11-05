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
		
restaurant = Restaurant('рога и копыта', 'международная')
restaurant.count_number_served()
restaurant.set_numver_served(25)
restaurant.count_number_served()
restaurant.increment_number_served(-500)
restaurant.count_number_served()
