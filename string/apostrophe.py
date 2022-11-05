message="One of the Python's strengths is its diverse community."
print(message)
 
name='Эрик'
print(f"Hello {name}, whould you like to learn some Python today?")
print(name.upper()) #тут меняется регистр букв
print(name.lower())
print(name.title())

famous_person="Albert Einstein"
message2=f'{famous_person} once said: "A person who never made a mistake never tried anything new"'
print(message2)

name_test=" Эрик  "
print(f"\n\n\t{name_test}") #\n это переход на новую строку а \t табуляция
print(name_test.lstrip()) #убирает пробелы слева
print(name_test.rstrip())
print(name_test.strip())
