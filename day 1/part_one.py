with open("res/masses", 'r') as file:
	masses = list(map(int, file.readlines()))
'''
Replace "res/expense report" with the path to your file containing the inputs or
replace "file.readlines()" with a string containing the inputs
'''

fuelRequired = 0

for mass in masses:
	fuelRequired += int(mass / 3) - 2

print("Total fuel required: " + str(fuelRequired))