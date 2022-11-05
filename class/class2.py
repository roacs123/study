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
		
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#ИЗМЕНЕНИЕ ЗНАЧЕНИЙ АТРИБУТОВ
#прямое изменение
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#изменение с использованием метода
my_new_car.update_odometer(25)
my_new_car.read_odometer()

#изменение значения атрибута с приращением
my_used_car = Car('toyota', 'camry', 2007)
print(my_used_car.get_descriptive_name())
my_used_car.increment_odometer(300100)
my_used_car.read_odometer()
my_used_car.increment_odometer(-100) #проверка
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
