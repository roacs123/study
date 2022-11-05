favorite_numbers={'Mike':[10,5,7,3], 'Sam':[5,3,1,111], 'Nick':[7,9,76,44], 'Jack':[5,44,444,100]}
for name, numbers in favorite_numbers.items():
	print(f"\nFavorite {name}'s numbers are:")
	for number in numbers:
		print(number)

cities = {'Moscow':
	{'country':'Russia', 'population':15000032, 'fact':'river Moscow'},
	'Perm':{'country':'Russia', 'population':1200303, 'fact':'river Kama'},
	'Sant-Petersburg':{'country':'Russia', 'population':5001003, 'fact': 'river Moyka'},
	}
for city, info in cities.items():
	print(f"\nInformation about: {city}")
	country = info['country']
	population = info['population']
	fact = info['fact']
	print(f"Country = {country}, population = {population}, fact = {fact}")
	
	 
	
