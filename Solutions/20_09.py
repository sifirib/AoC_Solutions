f = open("20_09_inputs", "r")
port_outputs = [int(num.strip()) for num in f.readlines()]
f.close()

# part 1
def is_producible(num):
    for i, num_ in enumerate(previous_nums):
        for num__ in previous_nums[i:]:
            if num_ + num__ == num:
                return True
    return False

def solve_part1():
    previous_nums = []
    index = 25 # starts with 26th number
    for num in port_outputs[25:]:
        previous_nums = port_outputs[index-25:index]
        index += 1
        if is_producible(num) == False:
            return num

# part 2
def solve_part2():
    for i, num in enumerate(port_outputs):
        sum_ = num
        aux_nums = [num]
        for num_ in port_outputs[i+1:]:
            aux_nums.append(num_)
            sum_ += num_
            if sum_ == invalid_num:
                return min(aux_nums) + max(aux_nums)

invalid_num = solve_part1()
print("part 1 answer is: ", invalid_num)
the_weakness = solve_part2()
print("part 2 answer is: ", the_weakness)


