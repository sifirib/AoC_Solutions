f = open("20_02_inputs", "r")
inputs = [line.strip() for line in f.readlines()]

#part one
def make_data_readable(data):
    limits, letter, password =  data.split(" ")
    bottom_limit, top_limit = limits.split("-")
    letter = letter[0]
    
    return int(bottom_limit), int(top_limit), letter, password

#def is_valid(bottom_limit, top_limit, letter, password):
#    password = [i for i in password]
#    counter = 0
#    for i in password:
#        if letter == i:
#            counter += 1
#    if bottom_limit <= counter <= top_limit:
#        return True
#    else:
#        return False

#counter = 0
#for input_ in inputs:
#    bottom_limit, top_limit, letter, password = make_data_readable(input_)
#    if is_valid(bottom_limit, top_limit, letter, password):
#        counter += 1       
#print(counter)
    
    

#part two
def is_valid(first_num, second_num, letter, password):
    password = [i for i in password]
    if (password[first_num - 1] == letter and password[second_num - 1] == letter) or (password[first_num - 1] != letter and password[second_num - 1] != letter):
        return False
    else:
        return True

counter = 0
for input_ in inputs:
    first_num, second_num, letter, password = make_data_readable(input_)
    if is_valid(first_num, second_num, letter, password):
        counter += 1
        
print(counter)