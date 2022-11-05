players=['charlie', 'mikhael', 'martina', 'eli']
print(players[0:3]) #печать среза списка
print(players[:2]) #срез начинается сначала
print(players[2:]) #срез до конца
print(players[-3:]) #срез последних трех игроков

print("Here are the first three players of my team:")
for player in players[:3]:
	print(player.title())

my_food=["pizza","pasta","carrot","cucumber"]
friends_food=my_food[:] #копирование списка
my_food.append('burger')
friends_food.append('sushi')
print(f"My favorite foods are: {my_food}")
print(f"\nMy friend's favorite foods are: {friends_food}")

my_food=["pizza","pasta","carrot","cucumber"]
friends_food=my_food #связывание списков(не надо так делать)
my_food.append('burger')
friends_food.append('sushi')
print(f"\nMy favorite foods are: {my_food}")
print(f"My friend's favorite foods are: {friends_food}")
print(f"\n\nThe first three items in the list are: {my_food[:3]}")
print(f"\n\nThree items in the middle of the list are: {my_food[1:4]}")
print(f"\n\nThe last three items in the list are: {my_food[-3:]}")

pizza=['margarita', 'peperoni', 'quatro_formaggi', 'vegetarian']
friends_pizza=pizza[:]
pizza.append("il'patio")
friends_pizza.append('meat')
print(f"My favorite pizzas are:{pizza}. \nMy friend's favorite pizzas are{friends_pizza}.")
for one_pizza in pizza:
	print(one_pizza)
