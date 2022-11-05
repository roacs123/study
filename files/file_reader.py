#конструкция которая открывает файл, заносит данные в переменную и когда нет необходимости закрывает файл
#ОТНОСИТЕЛЬНЫЙ ПУТЬ
with open('text_files/pi_digits.txt') as file_object: 
	contents = file_object.read()
	print(contents.rstrip()) #удаляет тот символ в конце строки который должен быть удален, по умолчанию пробел
#АБСОЛЮТНЫЙ ПУТЬ
file_path = 'C:/Users/roacs/Desktop/python_work/files/text_files/pi_digits.txt'
with open(file_path) as file_object: 
	contents = file_object.read()
	print(contents.rstrip())
#ПЕЧАТЬ ПОСТРОЧНО
with open(file_path) as file_object: 
	for line in file_object:
		print(line.rstrip())
#СОЗДАНИЕ СПИСКА ИЗ СТРОК
with open(file_path) as file_object: 
	lines = file_object.readlines() #метод читает последовательно 
for line in lines:                  # строку и сохраняет в списке
	print(line.rstrip())

#РАБОТА С СОДЕРЖИМЫМ ФАЙЛА
pi_string = ' '
for line in lines:
	pi_string += line.strip() #удаляет пропуски с двух сторон
print(float(pi_string)) #делает из строки с точкой число но окргуляет
print(len(pi_string))

file_path2 = 'C:/Users/roacs/Desktop/python_work/files/text_files/pi_million_digits.txt'
pi_string = ' '
with open(file_path2) as file_object: 
	lines = file_object.readlines()  
for line in lines:                  
	pi_string += line.strip()
print(pi_string[:52].lstrip() + "...")
#print(len(pi_string))

#ПРОВЕРКА ДНЯ РОЖДЕНИЯ
birthday = input("Enter your birthday, in form mmddyy: ")
if birthday in pi_string:
	print("Ваш день варенья там есть")
else:
	print("Дня варенья там нет")
