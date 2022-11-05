
#ПЕРЕДАЧА СПИСКА
def greet_users(names):
	"""Вывод простого приветствия для каждого пользователя в списке"""
	for name in names:
		msg = f"Hello, {name.title()}!"
		print(msg)
usernames = ['Anna', 'maria', 'kim']
greet_users(usernames)

#ИЗМЕНЕНИЕ СПИСКА В ФУНКЦИИ
#вариант без функции
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}.")
	completed_models.append(current_design)
print(f"The following models have been printed:")
for completed_model in completed_models:
	print(completed_model)

#с функциями
def print_models(unprinted_designs, completed_models):
	"""
	Имитирует печать моделей, пока список не станет пустым.
	Каждая модель после печати перемещается в comleted_models
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Выводит информацию обо всех напечатанных моделях."""
	print(f"The following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []		
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#ЗАПРЕТ ИЗМЕНЕНИЯ СПИСКА В ФУНКЦИИ
#для того чтобы элементы не удалились из первого списка вызымаем его копию
print_models(unprinted_designs[:], comleted_models)


