def make_pizza(size, *toppings):
	"""Выводит описание пиццы"""
	print(f"Making a {str(size)}cm pizza with the following toppings:")
	for topping in toppings:
		print(topping)
