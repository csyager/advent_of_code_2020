import json

with open('input.txt') as f:
    input_file = f.readlines()
input_file = [x.rstrip() for x in input_file]

bag_dict = {}

for elem in input_file:
    elem_list = elem.split()
    outer_bag = elem_list[0] + " " + elem_list[1] + " " + elem_list[2]
    inner_bag_list = []
    curr = ""
    for word in elem_list[5:]:
        if word.isnumeric():
            if ',' in curr or '.' in curr:
                curr = curr[:-1]
            inner_bag_list.append(curr[1:])
            curr = ""
        else:
            curr += " " + word
    inner_bag_list.append(curr[1:-1])
    bag_dict[outer_bag] = inner_bag_list

# print(json.dumps(bag_dict))

def find_bags_containing(bag_name):
    ret = []
    for bag in bag_dict:
        if bag_name in bag_dict[bag] or bag_name[:-1] in bag_dict[bag]:
            ret.append(bag)
    return ret

final_list = []

def find_bags_recursive(bag_list):
    if bag_list:
        count = 0
        for elem in bag_list:
            final_list.append(elem)
            find_bags_recursive(find_bags_containing(elem))

find_bags_recursive(find_bags_containing("shiny gold bags"))
final_list = list(dict.fromkeys(final_list))
print(final_list)
print(len(final_list))
