#КЛАСС РОДИТЕЛЬ (супер класс)
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

#КЛАСС КАК АТРИБУТ
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
			
#СОЗДАНИЕ КЛАССА ПОТОМКА (суб класс)			
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
		
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
new_car = ElectricCar('Лада', 'седан', 1995)
print(new_car.get_descriptive_name())
new_car.battery.get_range()
new_car.battery.upgrade_battery()
new_car.battery.get_range()



