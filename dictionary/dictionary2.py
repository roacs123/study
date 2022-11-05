favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
	'phil':'python',
	}
print(favorite_languages)
print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")
#запрашиваем значение по ключу

man={'age':20, 'height':180,
	'first_name':'Ivan', 'last_name':'Sidorov',
	 'city':'Moscow',
	 } 
print(man)

favorite_numbers={'Mike':10, 'Sam':5, 'Nick':7, 'Jack':100}
for name in favorite_numbers.keys():
	print(f"\nFavorite {name}'s number is {favorite_numbers.get(name)}.")
#создаем строку с привязкой значения к ключу

user_0 = {'username':'efermi',
	'first':'enrico',
	 'last':'fermi',
	 }
for key, value in user_0.items(): #обращение к ключу и значению внутри словаря
	#создание двух переменных берущих в себя ключ и значение
	print(f"\nKey: {key}")
	print(f"Value: {value}")

for name, language in favorite_languages.items():
	print(f"Favorite {name.title()}'s language is {language.title()}")

for name in favorite_languages.keys():
	print(name.title()) #перебор всех ключей
	
friends=['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends: #проверка наличия имени в списке 
		print(f"Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!")
		
if 'erin' not in favorite_languages.keys(): 
#проверка отсутствия имени в списке ключей
	print("\nErin, please take our poll!") 
