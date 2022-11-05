#СОЗДАНИЕ КЛАССА
class Dog(): #с большой буквы и скобки пусты потому что класс с нуля
	"""Простая модель собаки"""
	def __init__(self, name, age): #метод, автоматически выполняется
		#параметр self обязательный и первый - ссылка на экземпляр
		"""Инициализирует атрибуты name и age."""
		self.name = name
		self.age = age
		
	def sit(self): #метод
		"""Собака садится по команде"""
		print(f"{self.name.title()} is now sitting.")
		
	def roll_over(self): #метод
		"""Собака перекатывается по команде"""
		print(f"{self.name.title()} rolled over!")

#СОЗДАНИЕ ЭКЗЕМПЛЯРА КЛАССА
my_dog = Dog('bobik', 6)
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

#СОЗДАНИЕ НЕСКОЛЬКИХ ЭКЗЕМПЛЯРОВ
your_dog = Dog('tuzik', 3)
print(f"Your dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()

#УПРАЖНЕНИЯ
class Restaurant():
	"""Модель ресторана"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Инициализирует атрибуты название ресторана и тип кухни"""
		self.r_name = restaurant_name
		self.c_type = cuisine_type
	
	def describe_restaurant(self):
		"""Описывает ресторан"""
		print(f"Название ресторана {self.r_name.title()}, а кухня там {self.c_type}.")
	
	def open_restaurant(self):
		"""Открытие ресторана"""
		print(f"Ресторан {self.r_name.title()} открыт!")
		
restaurant = Restaurant('рожки да ножки', 'грузинская')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant2 = Restaurant('пивальди', 'международная')
restaurant2.describe_restaurant()

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
		
user1 = User('Иван', 'Иванов', 25, 'Россия')
user2 = User('Петя', 'пупкин', 28, 'беларусь')	
user1.describe_user()
user2.describe_user()
user1.greet_user()
user2.greet_user()
user1.increament_login_attempts()
user1.increament_login_attempts()
user1.increament_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
