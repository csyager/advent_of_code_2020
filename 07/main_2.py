import json

with open('input.txt') as f:
    input_file = f.readlines()
input_file = [x.rstrip() for x in input_file]

bag_dict = {}

for elem in input_file:
    elem_list = elem.split()
    key = ""
    for i in range(0, 3):
        key += elem_list[i] + " "
    key = key[:-1]
    curr = ""
    curr_list = []
    for i in range(4, len(elem_list)):
        curr += elem_list[i] + " "
        if i != 4 and (i+1)%4 == 0:
            curr_list.append(curr[:-2])
            curr = ""
    bag_dict[key] = curr_list

def count_bags(bag_name):
    print(bag_name)
    sum = 1
    for bag in bag_dict[bag_name]:
        factor = int(bag.split()[0])
        name = ""
        for word in bag.split()[1:]:
            name += word + " "
        name = name[:-1]
        if name[-1:] != 's':
            name += 's'
        sum += factor * count_bags(name)
    return sum

print(count_bags("shiny gold bags")-1)
# print(json.dumps(bag_dict))