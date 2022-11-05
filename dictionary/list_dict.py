alien_0={'color':'green', 'points':5}
alien_1={'color':'yellow', 'points':10}
alien_2={'color':'red', 'points':15}
aliens=[alien_0,alien_1,alien_2] #объединение трех словарей в список
for alien in aliens:
	print(alien)

aliens=[]
#Создание 30 зеленых пришельцев
for alien_number in range(30):
	new_alien={'color':'green', 'points':5, 'speed':'slow'}
	aliens.append(new_alien)
#Вывод первых 5 пришельцев:
for alien in aliens[:5]:
	print(alien)
print("...")
#вывод количества созданных пришельцев
print(f"Total number of aliens: {str(len(aliens))}.")

#меняем характеристики пришельцев
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
		
print("\n")
for alien in aliens[:5]:
	print(alien)
	

