#Программа загружает имя пользователя если оно было если нет то запрашивает 
#CОХРАНЕНИЕ И ЧТЕНИЕ ДАННЫХ
import json
"""filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print(f"We'll remember you when you come back {username}!")
else:
	print(f'Welcome back {username}!')	

#РЕФАКТОРИНГ разбитие кода на функции

def greet_user():
	Приветствует пользователя по имени.
	filename = 'username.json'
try:
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	username = input("What is your name? ")
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
		print(f"We'll remember you when you come back {username}!")
else:
	print(f'Welcome back {username}!')"""
	
 #Разбитие функции на три	
 
def get_stored_username():
	"""Получает хранимое имя пользователя, если оно существует."""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username
		
def get_new_username():
	"""Запрашивает новое имя пользователя"""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username
	
def greet_user():
	"""Приветствует пользователя по имени."""
	username = get_stored_username()
	while True:
		question = input(f"Ваше имя - {username}? (да,нет) ")
		if question == 'да':
			break
		else:
			username = get_new_username()
			print(f"We'll remember you when you come back {username}!")
	if username:
		print(f"Welcome back, {username}!")
	
		
greet_user()	
