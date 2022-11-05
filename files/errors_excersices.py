print("Введите два числа для сложения")
print("Для выхода напишите 'q'")
while True:
	first_number = input("Введите первое число: ")
	if first_number == 'q':
		break
	else:
		second_number = input("Введите второе число: ")
		if first_number == 'q':
			break
		else:
			try:
				summ = int(first_number) + int(second_number)
			except ValueError:
				print("Одно из значений не является числом")
			else:
				print(f"Сумма чисел равна {summ}")

def read_txt(filename):
	"""Читает содержимое текстовых файлов"""
	try:
		with open(filename, 'r', encoding='utf-8') as f_obj:
			content = f_obj.read()
	except FileNotFoundError:
		print(f"Файла {filename} не существует!") #pass если без уведомления	
	else:
		content = content.split()
		for cont in content:
			print(cont)
txt_files = ['cats.txt', 'dogs.txt', 'animals.txt']
for file in txt_files:
	read_txt(file)

def count_words(filename, word):
	"""Считает количество вхождений слова в документ"""
	with open(filename, 'r', encoding='utf-8') as f_obj:
		content = f_obj.read()
		counter = content.lower().count(word) #считает количество слов в документе
		print(f"В документе {filename} - {str(counter)} слов {word}")
		
count_words('women.txt', 'the')
