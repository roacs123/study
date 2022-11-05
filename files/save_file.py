#ЗАПИСЬ В ФАЙЛ
filename = 'programming.txt'
#если файла нет то он будет создан
#если в файле есть данные они исчезнут
with open(filename, 'w') as file_object: #файл открыт в режиме записи w
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.")

#ПРИСОЕДИНЕНИЕ ДАННЫХ К ФАЙЛУ
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
#УПРАЖНЕНИЯ
guestname = 'guest.txt'
with open(guestname, 'a') as file_object:
	guest = input('Введите ваше имя: ')
	file_object.write(str(guest)+'\n')

questbook = 'questbook.txt'
with open(questbook, 'a') as file_object:
	while True:
		questname = input("Для выхода напишите 'q' \nВведите ваше имя: ")
		if questname == 'q':
			break
		else:
			print(f"Приветствую тебя о, {questname}!")
			file_object.write(f"Приветствую тебя о, {str(questname)}!\n")
		
questions = 'questions.txt'
with open(questions, 'a') as file_object:
	while True:
		quest = input('Почему вам нравится программировать? ')
		print('Для выхода напишите "exit"')
		if quest == 'exit':
			break
		else:
			file_object.write(str(quest)+ "\n")
