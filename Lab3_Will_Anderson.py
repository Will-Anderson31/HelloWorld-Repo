income = int(input("Enter your earned income: "))
print("Are your married or single?")
marital = input("Type m for married and s for single: ")

if marital == "m":
	if (0 <= income <= 22000):
		print("This year you owe", f'{income * .1:.2f}', "in taxes")
	
	elif (22001 <= income <= 89450):
		print("This year you owe", f'{((income - 22000) * .12) + 2200:.2f}', "in taxes")
	
	elif (89451 <= income <= 190750):
		print("This year you owe", f'{((income - 89450) * .22) + 10294:.2f}', "in taxes")
		
	else:
		print("You made too much for this calculator. Hurray!")
		
elif marital == "s":
	if (0 <= income <= 11000):
		print("This year you owe", f'{income * .1:.2f}', "in taxes")
	
	elif (11001 <= income <= 44725):
		print("This year you owe", f'{((income - 11000) * .12) + 1100:.2f}', "in taxes")
	
	elif (44725 <= income <= 95375):
		print("This year you owe", f'{((income - 44725) * .22) + 5147:.2f}', "in taxes")
		
	else:
		print("You made too much for this calculator. Hurray!")
