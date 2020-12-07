f = open("20_01_inputs", "r")
numbers = [int(number.strip()) for number in f.readlines()]

#part one
#[print(numbers[i] * numbers[j]) for i in range(0, len(numbers)) for j in range(i, len(numbers)) if numbers[i] + numbers[j] == 2020]

#part two
[print(numbers[i] * numbers[j] * numbers[k]) for i in range(0, len(numbers)) for j in range(i, len(numbers)) for k in range(j, len(numbers)) if numbers[i] + numbers[j] + numbers[k] == 2020]
