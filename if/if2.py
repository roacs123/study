age=19
if age>=19:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")

age =17
if age>=19:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")	
else:
	print("\nSorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")
	
age=66
if age<4:
	print("Your admission cost is $0.")
elif age<18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

if age<4: #другой вариант
	price=0
elif age<18:
	price=5
elif age<65:
	price=10
else: #блок необязателен для цепочки if
	#можно заменить на elif age>=65:
	price=5
print(f"Your admission cost is ${str(price)}.")

requested_toppings=['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
	print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")
print("\nFinished making your pizza!")




