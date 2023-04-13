# ask for age
print("How Old Are You?")
age = input()
if age:
	age = int(age)
	# 18-21 wristband
	if age >= 18 and age < 21:
		print("You can enter but you need a wristband.")

	# 21+ drink, normal entry
	elif age >= 21:
		print("You are good to enter and have a nice drink today bud")
	# too young sorry
	else:
		print("Sorry youngling you are not allowed to enter :(")
else:
	print("please enter an age")