dimensions=(200,50) #кортеж, неизменяемый список
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
	print(dimension)
print(f"Original dimensions: {dimensions}")
dimensions=(400,100) #замена кортежа
print(f"Modified dimensions: {dimensions}")

