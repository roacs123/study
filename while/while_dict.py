unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users: #выполняется пока в списке остаются элементы
	#функция извлекает последнего пользователя из списка
	current_user = unconfirmed_users.pop() 
	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)
print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
#цикл продолжается пока элемент остаётся в списке
while 'cat' in pets:
	pets.remove('cat')
print(pets)

#заполнение словаря данными пользователя
responses = {}
#флаг продолжения опроса
polling_active = True
while polling_active:
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	#ответ сохраняется в словаре
	responses[name] = response
	#проверка продолжения опроса
	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False
#опрос завершён, вывод результатов
print("\n---Poll Results---")
for name, response in responses.items():
	print(f"{name.title()} would like to climb {response}.")
