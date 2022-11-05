def sandwich(*toppings):
	"""Выводит ингредиенты бутера"""
	print(f"В бутерброде будут такие ингридиенты: ")
	for topping in toppings:
		print(topping)
sandwich('сыр','колбаса','хлеб','масло')

def build_profile(first_name, last_name, **other_info):
	"""Создаёт профиль пользователя"""
	user = {}
	user['имя'] = first_name
	user['фамилия'] = last_name
	for key, value in other_info.items():
		user[key] = value
	return user
new_user = build_profile('биба', 'иванов', возраст=20, рост=180, вес=80)
print(new_user)


		
