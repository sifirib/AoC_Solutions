f = open("20_03_inputs", "r")
squares = [line.strip() for line in f.readlines()]

#part one
#i = j = counter = 0
#while j < len(squares):
#	if squares[j][i] == "#":
#		counter += 1
#	i += 3
#	j += 1
#	if i > len(squares[0]) - 1:
#		i = i - len(squares[0])
#print(counter)


#part two
result = 1
for k in range(0, 5):
	i = j = counter = 0
	if k == 0:
		i_add = 1
		j_add = 1
	if k == 1:
		i_add = 3
		j_add = 1
	if k == 2:
		i_add = 5
		j_add = 1
	if k == 3:
		i_add = 7
		j_add = 1
	if k == 4:
		i_add = 1
		j_add = 2
	while j < len(squares):
		if squares[j][i] == "#":
			counter += 1
		i += i_add
		j += j_add
		if i > len(squares[0]) - 1:
			i = i - len(squares[0])
	result *= counter
	
print(result)

