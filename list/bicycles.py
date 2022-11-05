bicycles=['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1]) #последний элемент списка
message=f'My first bicycle was a {bicycles[0].title()}'
print(message)

cars=['toyota', 'nissan', 'honda']
print(f"Я хотел бы мотоцикл {cars[-1]}.")
cars[1]='suzuki' #замена элемента списка
print(cars)

cars.append('nissan') #добавление элемента списка
print(cars)

motorcycles=[]
motorcycles.append('honda') #добавление элементов в пустой список
motorcycles.append('suzuki')
motorcycles.append('yamaha')
print(motorcycles)
motorcycles.insert(2, 'ducati') #добавление элемента внутрь списка
print(motorcycles)

del motorcycles[1] #удаление элемента списка 
print(motorcycles)

popped_motorcycle=motorcycles.pop() #убираем последний элемент из списка и вставляем его в переменную
print(motorcycles)
print(f"The last motorcycle I owned was a {popped_motorcycle}")

first_owned=motorcycles.pop(0) #вынимаем первый элемент из списка
print(f'The first motorcycle I owned was a {first_owned.title()}.') 

cars.remove('toyota') #удаление элемента списка по значению
print(cars)

print(bicycles)
too_expensive='trek'
bicycles.remove(too_expensive) #вывод причины удаления
print(bicycles)
print(f'\nA {too_expensive} is too expensive for me.')
