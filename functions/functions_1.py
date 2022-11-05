def greet_user():
	"""Выводит простое приветствие""" #строка документации
	print("Hello!")
greet_user()

def greet_user(username):
	"""Выводит простое приветствие"""
	print(f"Hello, {username.title()}!")
greet_user('jesse')

def favorite_book(title):
	print(f"One of my favorite books is {title}.")
favorite_book('IT')

#ПОЗИЦИОННЫЕ АРГУМЕНТЫ 
def describe_pet(animal_type, pet_name):
	"""Выводит информацию о животном"""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet('cat', 'murzik')

#ИМЕНОВАННЫЕ АРГУМЕНТЫ
describe_pet(animal_type = 'dog', pet_name = 'bobik') 
describe_pet(pet_name = 'bobik', animal_type = 'dog',)

#ЗНАЧЕНИЯ ПО УМОЛЧАНИЮ
def describe_pet1(pet_name, animal_type='dog'): #важно аргумент по умолчанию ставить в конце
	"""Выводит информацию о животном."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet1(pet_name = 'Bobik')
describe_pet1('Bobik')

#ЭКВИВАЛЕНТНЫЕ ВЫЗОВы ФУНКЦИИ
describe_pet1('willie')
describe_pet1(pet_name = 'willie')
describe_pet1('harry', 'hamster')
describe_pet1(pet_name = 'harry', animal_type = 'hamster')
describe_pet1(animal_type = 'hamster', pet_name = 'harry')

#УПРАЖНЕНИЯ
def make_shirt(text = 'I love Python!', size = 'L'):
	print(f"Необходима футболка размера {size}, с текстом: {text}")
make_shirt('Hello world!', 'XL')
make_shirt(text = 'WOW', size = 'L')
make_shirt()	
