f = open('20_06_inputs', 'r')
inputs = [input_.strip() for input_ in f.readlines()]
groups = []

i = 0
for input_ in inputs:
	if input_ == "":
		i += 1
	else:
		if len(groups) - 1 < i:
			groups.append("")
		groups[i] = groups[i] + " " + input_

i = 0
groups_seperated = []
for group in groups:
	j = 0
	for person in group.split():
		if len(groups_seperated) - 1 < i:
			groups_seperated.append({})
		groups_seperated[i][j] = person
		j += 1
	i += 1

#part one
#def control_answers(person):
#	answers = []
#	for answer in person.values():
#		for letter in answer:
#			if not letter in answers:
#				answers.append(letter)
#	return len(answers)


#part two
def control_answers(group):
	persons_answers = group.values()
	answers = []
	for answer in persons_answers:
		
		for letter in answer:
			answers.append(letter)
	counter = 0
	old_answers = []
	for answer in answers:
		if answers.count(answer) == len(group) and answer not in old_answers:
			old_answers.append(answer)
			counter += 1
	return counter

sum = 0
for group in groups_seperated:
	sum += control_answers(group)
print(sum)





