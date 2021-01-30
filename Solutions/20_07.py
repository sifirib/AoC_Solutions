f = open("20_07_inputs", "r")
lines = [line.strip() for line in f.readlines()]
f.close()

bags = {}
single_bags = [line[:-28] for line in lines if line[-28:] == " bags contain no other bags."]

for line in lines:
    start_index = line.find("contain")
    bag = line[:(start_index - 6)]
    content = line[(start_index + 8):-1]
    content = content.split(", ")
    content = [con[:-5] for con in content]
    for con in content:
        num, color = con.split(" ", 1)
        if num.isdigit():  # Eliminating single-bag lines...
            if bags.get(bag) is None:
                bags[bag] = {}
            bags[bag].update({color:int(num)})
print(bags)
capacities = {}
for bag in single_bags:
    if capacities.get(bag) is None:
        capacities[bag] = ""
    capacities.update({bag:1})

loop = True
while loop:
    for bag, content in bags.items():
        capacity = 0
        counter = 0
        for bag_, quantity in content.items():
            if bag_ in capacities.keys():
                counter += 1
                capacity += quantity * capacities[bag_]
        # if counter == len(content):
        #     capacities[bag] = capacity
        capacities[bag] = capacity
    print(len(capacities), len(bags))
    if len(capacities) >= len(bags):
        loop = False

#part one
counter = 0
for capacity in capacities.values():
    if capacity >= capacities["shiny gold"]:
        counter += 1
print(counter)
