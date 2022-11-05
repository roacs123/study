alien_color='green'
if alien_color=='green':
	print("Вы заработали 5 очков")
	
alien_color='red'
if alien_color=='green':
	print("Вы заработали 5 очков")
elif alien_color=='yellow':
	print("Вы заработали 10 очков")
elif alien_color=='red':
	print("Вы заработали 15 очков")

age=67
if age<2:
	print("Младенец")
elif 2<=age<4:
	print("Малыш")
elif 4<=age<13:
	print("Ребенок")
elif 13<=age<20:
	print("Подросток")
elif 20<=age<65:
	print("Взрослый")
elif 65<=age:
	print("Пожилой человек")

favorite_fruits=['apple', 'banana', 'pineapple', 'watermelon', 'cherry']
if 'apple' in favorite_fruits:
	print('You really like apples')
if 'watermelon' in favorite_fruits:
	print('You really like watermelons')
