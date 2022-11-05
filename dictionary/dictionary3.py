favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
	'phil':'python',
	}
for name in sorted(favorite_languages.keys()): #сортировка ключей по алфавиту
	print(f"{name.title()}, thank you for taking the poll.")

print(f"The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title()) #перебор всех значений
	
print(f"The following languages have been mentioned:")
for language in set(favorite_languages.values()): #set множество
	print(language.title()) #перебор всех неповторяющихся значений
	
rivers={'nile':'egypt', 'thames':'england', 'kama':'perm'}
for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}.")
for river in rivers.keys():
	print(river.title())
for country in rivers.values():
	print(country.title())
	
people=['jen', 'edward', 'max', 'sam']
for man in people:
	if man in favorite_languages.keys():
		print(f"{man.title()}, thank you for the poll.")
	else:
		print(f"{man.title()}, please take the poll.")
