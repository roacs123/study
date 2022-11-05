import unittest
import Employee from test_excersices2

class TestEmployee(unittest.TestCase):
	"""Тестирование класса Employee"""
	
	def setUp(self):
	"""Создание тестового экземпляра Employee"""
	self.test_admin = Employee('вася', 'пупкин', 1000)
	
	def test_give_default_raise(self):
		"""Проверяет повышение зарплаты по умолчанию"""
		
