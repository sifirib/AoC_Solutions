f = open("20_04_inputs", "r")
lines = [line.strip() for line in f.readlines()]

passports = []
i = 0
for line in lines:

	if line == "":
		i += 1
	else:
		if len(passports) - 1 < i:
			passports.append("")
		passports[i] = passports[i] + " " + line

persons = []
i = 0
for passport in passports:
	passport = passport.split()
	for pass_ in passport:
		pass_ = pass_.split(":")
		if len(persons) - 1 < i:
			persons.append({})
		persons[i][pass_[0]] = pass_[1]

	i += 1



#part one 
#def is_valid(passport):
#	is_ = True
#	if len(passport) == 7:
#		if "cid" in passport:
#			is_ = False
#	elif len(passport) < 7:
#		is_ = False
#
#	return is_

#counter = 0
#for passport in persons:
#	if is_valid(passport):
#		counter += 1
#print(counter)


#part two
def is_valid(passport):
	is_ = True
	if len(passport) == 7:
		if "cid" in passport:
			is_ = False
	elif len(passport) < 7:
		is_ = False

	if is_ == False:
		return is_
	else:

		if not (len(passport["byr"]) == 4 and 1920 <= int(passport["byr"]) <= 2002):
			return False
		if not (len(passport["iyr"]) == 4 and 2010 <= int(passport["iyr"]) <= 2020):
			return False
		if not (len(passport["eyr"]) == 4 and 2020 <= int(passport["eyr"]) <= 2030):
		    return False
		if not ((passport["hgt"][-2:] == "cm" and 150 <= int(passport["hgt"][:-2]) <= 193) or (passport["hgt"][-2:] == "in" and 59 <= int(passport["hgt"][:-2]) <= 76)):
		    return False
		if not (len(passport["hcl"][1:]) == 6 and passport["hcl"][1:].isalnum() and passport["hcl"][1:].islower()):
		    return False
		eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
		if not (passport["ecl"] in eye_colors):
		    return False
		if not (len(passport["pid"]) == 9 and passport["pid"].isdigit()):
		    return False
		return True
counter = 0
for passport in persons:
	if is_valid(passport):
		counter += 1
print(counter)
