#ввод информации пользователя
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"Hello, {name}!")

promt = "If you tell us who are you, we can personalize the message you see."
#+= объединяет текст 
promt += "\nWhat is your name? "
name = input(promt)
print(f"\nHello, {name.title()}!")

age = input("How old are you? ")
age = int(age) #преобразование строки в числовое значение
print(age)
print(age >= 18) #выводит true false

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")


