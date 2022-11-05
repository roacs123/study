for value in range(1,6):
	print(value)
	
numbers=list(range(1,6)) #преобразование в список
print(numbers)

even_numbers=list(range(2,11,2)) #вывод четных чисел от 2 до 10. третье значение шаг
print(even_numbers)

squares=[]
for value in range(1,11):
	square=value**2 #создание списка квадратов чисел от 1 до 11 
	squares.append(square)
print(squares)
print(min(squares)) #минимальное значение списка
print(max(squares)) #максимальное
print(sum(squares)) #сумма

squares2=[value**2 for value in range(1,11)] #генератор списка
print(squares2)

print("\n\n\n\n\n\n")
million=[]
for number in range(1,1000001):
	million.append(number)
print(min(million))
print(max(million))
print(sum(million))

nechet=[]
for number2 in range(1,21,2): #вывод списка нечетных чисел
	nechet.append(number2)
print(nechet)

triple=[]
for three in range(3,31,3): #вывод чисел кратных трём
	triple.append(three)
print(triple)

cubes=[value2**3 for value2 in range(1,11)] #генератор кубов для чисел от 1 до 10
print(cubes)
