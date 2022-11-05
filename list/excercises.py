guests=['Ivan', 'Maria', 'Elena', 'Anna']
for i in guests: #цикл для приглашения гостей
	print(f'{i.title()}, welcome to the party!')
sick_guest=guests.pop(0)
print(f'\t\t{sick_guest} прийти не сможет.')
guests.insert(0, 'Kate')
for i in guests: #цикл для приглашения новых гостей
	print(f'{i.title()}, welcome to the party!')
print('\t\tРасширение списка гостей')
guests.insert(0, 'Ivan')
guests.insert(2, 'Vladislav')
guests.append('Mikhail')
for i in guests: #цикл для приглашения новых гостей
	print(f'{i.title()}, welcome to the party!')
print('\t\tНа обед приглашаются только два гостя')
for i in range(1,6):
	deleted_guest=guests.pop(0)
	print(f'{deleted_guest.title()}, я сожалею об отмене приглашения')
for i in guests: #цикл для приглашения новых гостей
	print(f'{i.title()}, приглашение остаётся в силе!')
count=len(guests)
print(f"{count} человека приглашено на обед.")
for i in range(0,len(guests)):
	del guests[0]
print(guests)
