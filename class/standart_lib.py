from collections import OrderedDict #экземпляры класса отслеживают порядок добавления пар ключ значение
from random import randint

favorite_languages = OrderedDict()
favorite_languages['vova'] = 'python'
favorite_languages['sasha'] = 'c'
favorite_languages['gogi'] = 'ruby'
favorite_languages['petr'] = 'python'
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")
print(favorite_languages)

x = randint(1,6)
print(x)

class Die:
	"""Класс для тренировки стандартных библиотек"""
	def __init__(self, sides = 6):
		"""Инициализация данных"""
		self.sides = sides
	def roll_die(self):
		print(randint(1, self.sides))

kubik = Die()
for i in range(1,10):
	kubik.roll_die()

kubik10 = Die(10)
for i in range(1,10):
	kubik10.roll_die()


