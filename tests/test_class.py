class AnonymousSurvey():
	"""Сбор анонимных ответов на опросы."""
	
	def __init__(self, question):
		"""Сохраняет вопрос и готовится к сохранению ответов."""
		self.question = question
		self.responses = []
		
	def show_question(self):
		"""Выводит вопрос."""
		print(question)
		
	def store_response(self, new_response):
		"""Сохраняет один ответ на вопрос."""
		self.responses.append(new_response)
		
	def show_results(self):
		"""Выводит все полученные ответы."""
		print("Survey results:")
		for response in self.responses:
			print(f'- {response}')
"""
#определение вопроса с созданием экземпляра класса
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
#вывод вопроса  и сохранение ответов
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
	response = input("Language: ")
	if response == 'q':
		break
	my_survey.store_response(response)
#вывод результатов опроса
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
"""
