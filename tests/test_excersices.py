import unittest

def get_country_city(country, city, population=''):
	"""Функция возвращает строку в формате 'страна, город'"""
	if population:
		info = f"{country}, {city} население: {str(population)}"
	else:
		info = country + ', ' + city
	return info.title()

class CityCountryTest(unittest.TestCase):
	"""Тесты для функции get_country_city"""
	
	def test_city_country(self):
		"""Данные вида 'chile santiago' работают правильно?"""
		country_city = get_country_city('chile','santiago')
		self.assertEqual(country_city, 'Chile, Santiago')
	
	def test_city_country_population(self):
		country_city_population = get_country_city('chile', 'santiago', 15000000)
		self.assertEqual(country_city_population, 'Chile, Santiago Население: 15000000')

unittest.main()
