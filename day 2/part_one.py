with open("res/program1", 'r') as file:
	memory = list(map(int, file.readlines()[0].split(",")))
'''
Replace "res/expense report" with the path to your file containing the inputs or
replace "file.readlines()" with a string containing the inputs
'''

memory[1] = 12
memory[2] = 2

instructionPointer = 0
while(instructionPointer < len(memory)):
	opcode = memory[instructionPointer]
	if(opcode == 1):
		param0 = memory[instructionPointer+1]
		param1 = memory[instructionPointer+2]
		param2 = memory[instructionPointer+3]
		memory[param2] = memory[param0] + memory[param1]
		instructionPointer += 4
	elif(opcode == 2):
		param0 = memory[instructionPointer+1]
		param1 = memory[instructionPointer+2]
		param2 = memory[instructionPointer+3]
		memory[param2] = memory[param0] * memory[param1]
		instructionPointer += 4
	elif(opcode == 99):
		print(memory)
		exit()