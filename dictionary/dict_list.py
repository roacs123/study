#сохранение информации о заказанной пицце, список в словаре
pizza = {
	'crust':'thick',
	'toppings':['mushrooms', 'extra cheese'],
	}
#описание заказа
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
	print(f"\t{topping}") 
	
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil':['python', 'haskell'],
	}
for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print(f"{name.title()}'s favorite language is: {languages[0].title()}")
	else:
	    print(f"\n{name.title()}'s favorite languages are:")
	    for language in languages: 
		    print(f"\t{language.title()}")
