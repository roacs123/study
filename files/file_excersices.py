file_path = "C:/Users/roacs/Desktop/python_work/files/text_files/learning_python.txt"
with open(file_path) as file_object:
	content = file_object.read()
print(content)

with open(file_path) as file_object:
	for line in file_object:
		print(line.rstrip())
		
with open(file_path) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.replace('Python', 'java'))
	

 
