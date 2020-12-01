with open("res/masses", 'r') as file:
	masses = list(map(int, file.readlines()))

fuelRequired = 0

for mass in masses:
	fuelRequired += int(mass / 3) - 2

print("Total fuel required: " + str(fuelRequired))