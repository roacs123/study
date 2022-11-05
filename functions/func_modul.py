#ИМПОРТИРОВАНИЕ МОДУЛЯ КОТОРЫЙ В ОДНОМ КАТАЛОГЕ
import pizza
pizza.make_pizza(32, 'сыр','мясо','соус') #вызов функции из модуля
pizza.make_pizza(15, 'моцарелла', 'помидор')

#ИМПОРТИРОВАНИЕ КОНКРЕТНЫХ ФУНКЦИЙ
from pizza import make_pizza #через запятую можно еще функции

#НАЗНАЧЕНИЕ ПСЕВДОНИМА ДЛЯ ФУНКЦИИ
from pizza import make_pizza as mp
mp(20, 'сыр','оливки','колбаса')

#НАЗНАЧЕНИЕ ПСЕВДОНИМА ДЛЯ МОДУЛЯ
import pizza as p
p.make_pizza(50, 'сыр','сыр','сыр')

#ИМПОРТИРОВАНИЕ ВСЕХ ФУНКЦИЙ МОДУЛЯ
from pizza import *
make_pizza(10, 'только сыр')

#УПРАЖНЕНИЯ
import printing_functions as pf
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []		
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
