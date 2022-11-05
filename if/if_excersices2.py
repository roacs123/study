users=['admin', 'user1', 'king', 'Mike', 'Bob']
for user in users:
	if user=='admin':
		print("Hello admin, whould you like to see a status report?")
	else:
		print(f"Hello {user.title()}, thank you for logging in again.")

users2=[]
if users2:
	for user in users2:
		print(f"Hello {user}")
else:
	print("\nWe need to find some users!")

print("\n\n")

current_users=['mike', 'john', 'sam', 'nick', 'luke']
new_users=['Sam', 'Luke', 'Dan', 'Din', 'Woody']
for new_user in new_users:
	if new_user.lower() in current_users:
		print(f"{new_user} you should choose a new nickname")
	else:
		print(f"{new_user} is available!")

print("\n\n")

numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
	if number == 1:
		print(f"{number}st")
	elif number == 2:
		print(f"{number}nd")
	elif number == 3:
		print(f"{number}rd")
	else:
		print(f"{number}th")
