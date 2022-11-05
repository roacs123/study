#ПЕРЕДАЧА ПРОИЗВОЛЬНОГО НАБОРА АРГУМЕНТОВ
def make_pizza(*toppings): #создаётся пустой кортеж toppings
	"""Вывод списка заказанных дополнений."""
	print(f"\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print(topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#ПОЗИЦИОННЫЕ АРГУМЕНТЫ С ПРОИЗВОЛЬНЫМИ НАБОРАМИ АРГУМЕНТОВ
def make_pizza(size, *toppings): #произвольные аргументы в конце
	"""Вывод описания пиццы."""
	print(f"\nMaking a {str(size)}sm pizza with the following toppings:")
	for topping in toppings:
		print(topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#ИСПОЛЬЗОВАНИЕ ПРОИЗВОЛЬНОГО НАБОРА ИМЕННОВАННЫХ АРГУМЕНТОВ
def build_profile(first, last, **user_info): 
	"""Строит словарь с информацией о пользователе."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items(): #тут поиск произвольных аргументов
		profile[key] = value
	return profile
user_profile = build_profile('albert', 'einstein', 
	location = 'princeton',
	field = 'physics')
print(user_profile)
