import unittest
from test_excersices2 import Employee

class TestEmployee(unittest.TestCase):
	"""Тестирование класса Employee"""
	
	def setUp(self):
		"""Создание тестового экземпляра Employee"""
		self.test_admin = Employee('вася', 'пупкин', 1000)
	
	def test_give_default_raise(self):
		"""Проверяет повышение зарплаты по умолчанию"""
		self.test_admin.give_raise()
		self.assertEqual(self.test_admin.year_salary, 6000)
		
	def test_give_custom_raise(self):
		"""Проверяет повышение зарплаты по умолчанию"""
		self.test_admin.give_raise(2000)
		self.assertEqual(self.test_admin.year_salary, 3000)
		
unittest.main()
		
