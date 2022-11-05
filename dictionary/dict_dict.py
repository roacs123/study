#словарь в словаре
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	}
for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")

man={'age':20, 'height':180,
	'first_name':'Ivan', 'last_name':'Sidorov',
	 'city':'Moscow',
	 } 
man1={'age':40, 'height':170,
	'first_name':'Maria', 'last_name':'Ivanova',
	 'city':'Perm',
	 } 
man2={'age':10, 'height':160,
	'first_name':'Jason', 'last_name':'Stethem',
	 'city':'Los Angeles',
	 } 
people = [man, man1, man2]
for peop in people:
	full_name = peop['first_name'] + " " + peop['last_name']
	age = peop['age']
	city = peop['city']
	print(f"{full_name} with age: {age} lives in {city}")
	
mans=[]	
favorite_places = {
	'Moscow':['ivan', 'maria', 'ibragim'],
	'Leningrad':['artem', 'sveta', 'maria'],
	'Vladivostok':['ivan', 'gendos', 'viktor'],
	}
for city, names in favorite_places.items():
	for name in names:
		print(f"{name.title()}'s favorite place is {city}.")

#попытка 25 выдернуть ключ по значению
def get_key(d, value): #функция которая вынимает ключ по значению(не нужна)
	for k, v in d.items():
		for v1 in v:
			if v1 == value:
				return k

for names in favorite_places.values(): #тут создаем список всех имен словаря
	for name in names:
		mans.append(name)
print(mans)
	
def f(l): #функция которая убирает повторяющиеся элементы списка
	n=[]
	for i in l:
		if i not in n:
			n.append(i)
	return n
new_man=f(mans) #новый список без повторений
#тут наконец программа находит ключи по значению и выводит их
for new_man1 in new_man:
	print(f"{new_man1.title()}'s favorite place:")
	for city, names in favorite_places.items():
			if new_man1 in names:
				print(city) 


