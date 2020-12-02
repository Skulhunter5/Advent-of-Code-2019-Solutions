# Replace the following code block with how you want to load your inputs
with open("res/masses", 'r') as file:
	masses = list(map(int, file.readlines()))

fuelTotal = 0

for mass in masses:
	fuelModule = int(mass / 3) - 2
	step = fuelModule
	step = int(step / 3) - 2
	while(step > 0):
		fuelModule += step
		step = int(step / 3) - 2
	fuelTotal += fuelModule

print("Total fuel required: " + str(fuelTotal))