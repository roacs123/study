alien_0={'color':'green', 'points':5} #словарь ключи:значения
print(alien_0['color']) #элемент словаря
print(alien_0['points'])

new_points=alien_0['points']
print(f'You just earned {str(new_points)} points!')

alien_0['x_position']=0
alien_0['y_position']=25
print(f"\n{alien_0}")

alien_0={}
alien_0['color']='green' #добавление элементов
alien_0['points']=5
print(alien_0)
print(f"The alien is {alien_0['color']}.")
alien_0['color']='yellow' #смена значения ключа
print(f"The alien is {alien_0['color']}.")

alien_0={'x_position':0, 'y_position':25, 'speed':'medium', 'points':5}
print(f"Original x-position: {str(alien_0['x_position'])}")
#пришелец двигается вправо по оси x и вычисляем его смещение
alien_0['speed']='fast' #скорость изменилась на быструю
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
#новая позиция равна старой, плюс приращение
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x-position: {str(alien_0['x_position'])}")

del alien_0['points'] #удаление элемента словаря
print(alien_0)

