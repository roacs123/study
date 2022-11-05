promt = "Enter the name of a city you have visited:"
promt +="\nEnter 'quit' to end the program. "

while True: #бесконечный цикл до команды break
	city = input(promt)
	if city == 'quit':
		break #прерывание цикла, так же работает и в циклах for
	else:
		print(f"I'd love to go to {city.title()}!")
		
current_number = 0 #чтобы начался цикл while
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue #команда игнорирует оставшийся код цикла и возвращается к началу while
	print(current_number)

#бесконечный цикл! Ctrl+C выйти
x = 1
while x <= 5:
	print(x)
	break
	
msg = "Введите дополнительный ингридиент к пицце: "
msg +="\nEnter 'quit' to end the program. "
flag = True
while flag:
	ingridient = input(msg)
	if ingridient == 'quit':
		flag = False
	else:
		print(f"\n{ingridient.title()} будет добавлен в пиццу!")
	
#тут три варианта выхода из цикла	
msg = "Введите возраст посетителя: "
msg += "\nДля выхода напишие 'выход' "
flag = True
while flag: #как вариант while age =! 'выход' или while true до команды break
	age=input(msg)
	if age == 'выход':
		flag = False
	elif int(age) < 3:
		print("Вход бесплатный!")
	elif 3 <= int(age) <= 12:
		print("Вход стоит 10$")
	elif int(age) > 12:
		print("Вход стоит 15$")
	
