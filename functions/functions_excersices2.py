focusmans = ['Biba', 'Boba', 'Jack']
reverse = []
def show_magicians(focusmans):
	"""Перечисляет фокусников из списка"""	
	for focusman in focusmans:
		print(focusman)
show_magicians(focusmans)

def make_great(men):
	"""Прибавляет каждому фокуснику слово Great"""
	while men:
		focusman = men.pop()
		focusman = 'Great' + ' ' + focusman
		reverse.append(focusman)
	while reverse: #второй цикл чтобы развернуть порядок
		focusman = reverse.pop()
		men.append(focusman)
	return men
focusmans2 = make_great(focusmans[:]) #работает с копией списка
show_magicians(focusmans2)
show_magicians(focusmans)
