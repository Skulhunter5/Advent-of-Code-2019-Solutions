with open("res/masses", 'r') as file:
	masses = list(map(int, file.readlines()))
'''
Replace "res/expense report" with the path to your file containing the inputs or
replace "file.readlines()" with a string containing the inputs
'''

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