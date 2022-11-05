burgers = ['чизбургер','веганбургер','гамбургер','биг_тейсти','веганбургер','филе-о-фиш','чикенбургер']
finished_burgers = []
print("Веганбургеров больше нет")
while 'веганбургер' in burgers:
	burgers.remove('веганбургер')
while burgers:
	burger = burgers.pop()
	print(f"Я приготовил тебе: {burger}")
	finished_burgers.append(burger)
print("Список сделанных бургеров:")
for finished_burger in finished_burgers:
	print(finished_burger)

vacation = {}
flag = True
while flag:
	name = input("What is your name? ")
	country = input("Where do you want to go on the vacation? ")
	repeat = input("Another user? (yes/no) ")
	vacation[name]=country
	if repeat == 'no':
		flag = False
for name, country in vacation.items():		
	print(f"{name.title()}'s best place for vacation is {country.title()}")
		
