accumulator = 0
cur_offset = 0
def nop(value):
    global cur_offset
    cur_offset += 1
def jmp(value):
    global cur_offset 
    cur_offset += value
def acc(value):
    global accumulator
    global cur_offset 
    accumulator += value
    cur_offset += 1
def is_second_run(offset):
    return instructions[offset]["is_ran"]

f = open("20_08_inputs", "r")
broken_instructions = [{"operator":line.strip()[:3], "value":int(line.strip()[4:]), "is_ran":False} for line in f.readlines()]
f.close()

# part 1
#while is_second_run(cur_offset) == False:
#    ins = broken_instructions[cur_offset]
#    ins["is_ran"] = True
#    globals()[ins["operator"]](ins["value"])
#print("Accumulator value is:", accumulator)

instructions = broken_instructions
found = False
for i in range(0, len(instructions)):
    if instructions[i]["operator"] == "jmp":
        instructions[i]["operator"] = "nop"
    elif instructions[i]["operator"] == "nop":
        instructions[i]["operator"] = "jmp"
    j = 0
    accumulator = 0
    while (j <= len(instructions)):
        ins = instructions[cur_offset]
        ins["is_ran"] = True
        j += 1
        print(cur_offset)
        globals()[ins["operator"]](ins["value"])
        if cur_offset == len(instructions):
            found = True
            break
    if found == True:
        break
    instructions = broken_instructions
print("Accumulator value is:", accumulator)
