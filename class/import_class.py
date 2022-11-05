#from car import Car, ElectricCar открывает модуль car и импортирует класс
#или можно импортировать весь модуль import car
from restaurant import Restaurant
from car import Privileges, Admin, Car, ElectricCar

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla','model s', 2020)
print(my_tesla.get_descriptive_name())
my_tesla.battery. describe_battery()
my_tesla.battery.get_range()

cafe1 = Restaurant('крошка картошка', 'фаст фуд')
cafe1.describe_restaurant()

user001 = Admin('вася', 'пупкин', 55, 'Belarus')
user001.describe_user()
user001.privileges.show_privileges()



