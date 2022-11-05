cars=['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car=='bmw': #проверка равенства
		print(car.upper())
	else:
		print(car.title())	

requested_topping='mushrooms'
if requested_topping !='anchovies': #проверка неравенства
	print("Hold the anchovies!")

answer=17
if answer<=42:
	print('That is not the correct amswer. Please try again!')

age1=22
age2=25
if (age1>21) and (age2>21): #проверка двух условий одновременно
	print('Yes')

if (age1<23) or (age2>26): #если хотя бы одно из двух условий верно
	print('yes again')

if 'bmw' in cars: #проверка присутствия элемента в списке
	print('yes it is in')

banned_users=['andrew','carolina', 'david']
user='marie'

if user not in banned_users: #проверка отсутствия элемента в списке
	print(f"{user.title()}, you can post a response if you wish.")

car='subaru'
print("Is car == 'subaru'? I predict True.")
print(car=='subaru') #проверка соответствия 
print("\nIs car == 'audi'? I predict False.")
print(car=='audi')

print('\n\n')
test='Mustang'
count=5
testes=['odin', 'dva', 'tri']
print(test=='MUstang')
print(test.lower()=='mustang')
if len(test)>6:
	print('More than 6 letters')
if test=='Mustang' and count==5:
	print('super yes')
if 'odin' in testes:
	print('odin is in')
