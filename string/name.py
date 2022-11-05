name="lana ivanova"
print(name.title())#делает заглавными первые буквы
name="lana ivanova"
print(name.upper()) #все буквы заглавные
name="lana ivanova"
print(name.lower())

first_name='lana'
second_name='ivanova'
full_name=f"{first_name.title()} {second_name.title()}"
print(full_name)

first_name='lana'
second_name='ivanova'
full_name=f"\t{first_name.title()} {second_name.title()}"
print(full_name)

first_name='первая строчка'
second_name='вторая строчка'
full_name=f"{first_name.title()}\n\t{second_name.title()}"
print(full_name)

name=" lana ivanova "
name=name.rstrip() #удаление пробела справа
print(name)
name=name.lstrip() #удаление пробела слева
print(name)
name=name.strip() #удаление пробела с обеих сторон
print(name)
