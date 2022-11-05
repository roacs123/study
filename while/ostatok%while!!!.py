print(4%3) #оператор вычисляет остаток от деления, в данном примере 1
print(6%3) #а тут 0
# как вариант проверки на чётность
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
	print(f"\nThe number {str(number)} is even.")
else:
	print(f"The number {str(number)} is odd.")

message = "\nВведите число"
message += "\nПроверю его кратность 10: "	
number10 = input(message)
number10 = int(number10)
if number10%10 == 0:
	print("Число кратно десяти")
else:
	print("Число не кратно десяти")

current_number = 1
while current_number <= 5: #цикл который работает до того как станет 5
	print(current_number)
	current_number += 1

promt = "\nTell me something, and I will repeat it back to you:"
promt +="\nEnter 'quit' to end the program. "
message = " " #необходимое значение для работы программы
while message != 'quit': #пока сообщение не будет quit
	message = input(promt) 
	if message != 'quit': #проверка чтобы не вывести quit как текст
		print(message)

#теперь добавим флаг который будет true или false
promt = "\nTell me something, and I will repeat it back to you:"
promt +="\nEnter 'quit' to end the program. "
active = True
while active: #пока переменная остаётся true программа выполняется
	message = input(promt)
	if message == 'quit':
		active = False #флаг на завершение цикла while
	else:
		print(message)
		
		
