from restaurant import User
"""Класс для представления автомобиля"""
class Car():
	"""Простая модель автомобиля"""
	def __init__(self, make, model, year):
		"""Инициализирует атрибуты описания автомобиля."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0 #метод создаёт новый атрибут 
	
	def get_descriptive_name(self):
		"""Возвращает аккуратно отформатированное описание."""
		long_name = str(self.year) + ' ' + self.make + ' ' +self.model
		return long_name.title()
	
	def read_odometer(self):
		"""Выводит пробег машины в километрах"""
		print(f"{self.make.title()} {self.model.title()} has {str(self.odometer_reading)} kilometers on it.")
	
	def update_odometer(self, kilometers): #новый атрибут
		"""
		Устанавливает заданное значение на одометре.
		При попытке обратной подкрутки изменение отклоняется.
		"""
		if kilometers >= self.odometer_reading: #проверка на снижение пробега
			self.odometer_reading = kilometers
		else:
			print(f"You can't roll back an odometer!")
			
	def increment_odometer(self, km):
		"""Увеличивает показание одометра с заданным приращением"""
		if km <= 0:
			print('Нельзя скручивать пробег')
		else:
			self.odometer_reading += km
			
class Battery():
	"""Простая модель аккумулятора электромобиля."""
	def __init__(self, battery_size=70):
		"""Инициализирует атрибуты аккумулятора"""
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""Выводит информацию о мощности аккумулятора"""
		print(f"This car has a {str(self.battery_size)} kWh battery.")
		
	def get_range(self):
		"""Выводит приблизительный запас хода для аккумулятора"""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)
	
	def upgrade_battery(self):
		"""Проверяет мощность аккумулятора и устанавливает мощность 85"""
		if self.battery_size != 85:
			self.battery_size = 85
			
			
class ElectricCar(Car): #Имя класса родителя в скобках
	"""Представляет аспекты машины, специфические для электромобилей"""
	def __init__(self, make, model, year):
		"""Инициализирует атрибуты класса - родителя."""
		#функция которая помогает связать потомка с родителем
		super().__init__(make, model, year)
		self.battery = Battery() #создание экземпляра внутри класса
	
#Если у супер класса есть такой метод, то его можно переопределить в субклассе		
	def fill_gas_tank(): 
		"""У электромобилей нет бензобака"""
		print("This car doesn't need a gas tank!")
		
		
class Privileges():
	"""Привилегии пользователей"""
	def __init__(self, privileges= ['разрешено удалять пользователей', 'разрешено банить пользователей']):
		"""Инициирует атрибуты класса"""
		self.privileges = privileges
	
	def show_privileges(self):
		"""Вывод набора привелегий администратора"""
		print("Привилегии администратора:")
		for privilege in self.privileges:
			print(privilege)	
				
class Admin(User):
	"""Профиль администратора"""
	def __init__(self, first_name, last_name, age, country,):
		"""Инициализирует атрибуты класса родителя плюс привелегии"""
		super().__init__(first_name, last_name, age, country)
		self.privileges = Privileges()
