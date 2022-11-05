cars=['bmw', 'audi', 'subaru', 'toyota']
print(cars)
cars.sort() #сортировка по алфавиту 
print(cars)
cars.sort(reverse=True) #сортировка наоборот
print(cars)

print("Here is original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars)) #выводит список по алфавиту, но не сохраняет порядок
print("\nHere is the original list again")
print(cars)
cars.reverse()#вывод списка наоборот
print(cars) 
i=len(cars) #подсчёт количества элементов списка
print(i)
