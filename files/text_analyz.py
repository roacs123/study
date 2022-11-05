title = "Alice in Wonderland"
print(title.split()) #разделение на слова, по умолчанию пробел

filename = 'alice.txt'
try:
	with open(filename, 'r', encoding='utf-8') as f_obj: #чтобы читалась кодировка
		contents = f_obj.read()
except FileNotFoundError:
	msg = f"Извините, файла {filename} не существует"
	print(msg)
else:
	#Подсчёт приблизительного количества слов в файле
	words = contents.split()
	num_words = len(words)
	print(f"Файл {filename} содержит {str(num_words)} слов")
	
#РАБОТА С НЕСКОЛЬКИМИ ФАЙЛАМИ
def count_words(filename):
	"""Подсчёт приблизительного количества слова в файле."""
	try:
		with open(filename, 'r', encoding='utf-8') as f_obj: #чтобы читалась кодировка
			contents = f_obj.read()
	except FileNotFoundError:
		msg = f"Извините, файла {filename} не существует"
		print(msg)
	else:
	#Подсчёт приблизительного количества слов в файле
		words = contents.split()
		num_words = len(words)
		print(f"Файл {filename} содержит {str(num_words)} слов")
		
filenames = ['women.txt', 'alice.txt', 'abba.txt']
for file in filenames:
	count_words(file)
	
#ОШИБКИ БЕЗ УВЕДОМЛЕНИЯ ПОЛЬЗОВАТЕЛЯ
def count_words1(filename):
	"""Подсчёт приблизительного количества слова в файле."""
	try:
		with open(filename, 'r', encoding='utf-8') as f_obj: #чтобы читалась кодировка
			contents = f_obj.read()
	except FileNotFoundError:
		pass #без уведомления
	else:
	#Подсчёт приблизительного количества слов в файле
		words = contents.split()
		num_words = len(words)
		print(f"Файл {filename} содержит {str(num_words)} слов")
		
filenames = ['women.txt', 'alice.txt', 'abba.txt']
for file in filenames:
	count_words1(file)

