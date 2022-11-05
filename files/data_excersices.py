#ПРОГРАММА ЗАПИСИ И ЧТЕНИЯ ЛЮБИМОГО ЧИСЛА
import json

def get_new_number():
	"""Узнает любимое число у пользователя"""
	filename = 'favorite_number.json'
	with open(filename, 'w') as f_obj:
		favor_num = input("Введите ваше любимое число: ")
		json.dump(favor_num, f_obj)
	return favor_num

def get_stored_number():
	"""Загружает любимое число из памяти"""
	filename = 'favorite_number.json'
	try:
		with open(filename) as f_obj:
			favor_num = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return favor_num
		
def favorite_number():
	"""Сообщает любимое число пользователя"""
	favor_num = get_stored_number()
	if favor_num:
		print(f"Любимое число пользователя: {favor_num}.")
	else:
		get_new_number()

favorite_number()
		
	
