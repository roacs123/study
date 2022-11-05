def city_country(city, country):
	"""Возвращает город и страну"""
	print(f"{city.title()}, {country.title()}")
city_country('moscow', 'russia')
city_country('london', 'england')

def make_album(name, album, tracks=''):
	"""Возвращает словарь содержащий исполнителя и название альбома"""
	if tracks:
		album_dict = {'name' : name, 'album' : album,'tracks' : tracks}
	else:
		album_dict = {'name' : name, 'album' : album}
	return album_dict
metalica = make_album('metalica' , 'hate me')
print(metalica)
kino = make_album('kino', 'zvezda po imeni')
print(kino)
hleb = make_album('hleb', 'chaj', 40)
print(hleb)

while True:
	print("\nВведите данные исполнителя")
	print("Для выхода напишите 'q'")
	name = input("Введите название исполнителя: ")
	if name == 'q':
		break
	album = input("Введите название альбома: ")
	if album == 'q':
		break
	new_alb = make_album(name, album)
	print(new_alb)
	
	


