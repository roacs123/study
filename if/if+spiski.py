requested_toppings=['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping=='green peppers': #проверка элемента перед добавлением в пиццу
		print("Sorry, we are out of green peppers right now.")
	else:	
	    print(f"Adding {requested_topping}")
print("Finished making your pizza!")

requested_toppings=['cheese']
if requested_toppings: #проверка на наличие какого-либо элемента в списке
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
		print("\nFinished making your pizza!")
        
else:
	print("\nAre you sure you want a plain pizza?")

print('\n\n\n')
available_toppings=['mushrooms', 'olives', 'green peppers',
     'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings: #проверка на наличие элементов одного списка в другом
		print(f"Adding {requested_topping}")
	else:
		print(f"Sorry, we don't have {requested_topping}.")
print("Finished making your pizza!")
