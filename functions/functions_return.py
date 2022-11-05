def get_formatted_name(first_name, last_name):
	"""Возвращает аккуратно отформатированное полное имя."""
	full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#НЕОБЯЗАТЕЛЬНЫЕ АРГУМЕНТЫ
def get_formatted_name1(first_name, last_name, middle_name = ''):
	"""Возвращает акккуратно отформатированное полное имя"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name1('john', 'hooker', 'lee')
print(musician)
musician = get_formatted_name1('jimi', 'hendrix')
print(musician)

#ВОЗВРАЩЕНИЕ СЛОВАРЯ
def build_person(first_name, last_name, age = ''):
	"""Возвращает словарь с информацией о человеке."""
	person = {'first' : first_name, 'last' : last_name}
	if age:
		person['age'] = age
	return person
	
musician = build_person('jimi', 'hendrix', age = 27)
print(musician)

#ФУНКЦИЯ В ЦИКЛЕ WHILE
#Бесконечный цикл(позже сделан с выходом)
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	f_name = input("First name: ")
	if f_name == 'q': #проверка на прерывание цикла
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")
	
	
