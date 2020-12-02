# Replace the following code block with how you want to load your inputs
with open("program", 'r') as file:
	program = list(map(int, file.readlines()[0].split(",")))

for noun in range(100):
	for verb in range(100):
		memory = program.copy()
		memory[1] = noun
		memory[2] = verb

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
				if(memory[0] == 19690720):
					print(i, j)
					print(memory)
				break