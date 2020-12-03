# Replace the following code block with how you want to load your inputs
with open("route", 'r') as file:
	routes = file.readlines()

for route in routes:
	route.strip()

maxX = 0
maxY = 0
for route in routes:
	x = 1
	y = 1
	tokens = route.split(',')
	for token in tokens:
		direction = token[0]
		distance = int(token[1:])
		if(direction == 'U'):
			y += distance
		elif(direction == 'R'):
			x += distance
		elif(direction == 'D'):
			y -= distance
		elif(direction == 'L'):
			x -= distance
		if(x > maxX):
			maxX = x
		if(y > maxY):
			maxY = y

print(str(maxX) + " : " + str(maxY))
temp = input("Do you want to continue: ")
if(temp != 'yes'):
	exit()

grid = []
for i in range(maxX + 10):
	grid.append([])
	for j in range(maxY + 10):
		grid[i].append(False)

distances = []

x = 1
y = 1
for route in routes:
	tokens = route.split(',')
	for token in tokens:
		direction = token[0]
		distance = int(token[1:])
		if(direction == 'U'):
			for j in range(1, distance + 1):
				if(grid[x][y + j]):
					distances.append([x, y + j])
				else:
					grid[x][y + j] = True
			y += distance
		elif(direction == 'R'):
			for i in range(1, distance + 1):
				if(grid[x + i][y]):
					distances.append([x + i, y])
				else:
					grid[x + i][y] = True
			x += distance
		elif(direction == 'D'):
			for j in range(1, distance + 1):
				if(grid[x][y - j]):
					distances.append([x, y - j])
				else:
					grid[x][y - j] = True
			y -= distance
		elif(direction == 'L'):
			for i in range(1, distance + 1):
				if(grid[x + i][y]):
					distances.append([x + i, y])
				else:
					grid[x - i][y] = True
			x -= distance

minDistance = 1000000000
for distance in distances:
	if(distance < minDistance):
		minDistance = distance

print(minDistance)