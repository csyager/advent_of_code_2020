with open('input.txt') as f:
    input_file = f.readlines()
input_file = [x.rstrip() for x in input_file]
input_file = list(map(int, input_file))
input_file.sort()

max = input_file[0]
for elem in input_file[1:]:
    if elem > max:
        max = elem

device_jolts = max + 3

one_step_count = 0
two_step_count = 0
three_step_count = 0

if input_file[0] == 1:
    one_step_count += 1
elif input_file[0] == 2:
    two_step_count += 1
elif input_file[0] == 3:
    three_step_count += 1
else:
    print("Error, first adapter can't connect to source.")
    exit(-1)

for i in range(0, len(input_file)):
    elem = input_file[i]
    try:
        next_elem = input_file[i+1]
    except IndexError:
        print("End of list reached at element " + str(elem))
        next_elem = elem + 3

    if next_elem - elem == 3: 
        three_step_count += 1
        print(str(elem) + " -> " + str(next_elem) + " == three_step_count: " + str(three_step_count))
    elif next_elem - elem == 2:
        two_step_count += 1
        print(str(elem) + " -> " + str(next_elem) + ": " + str(two_step_count))
    elif next_elem - elem == 1:
        one_step_count += 1
        print(str(elem) + " -> " + str(next_elem) + ": == one_step_count: " + str(one_step_count))
    else:
        print("Error, step size greater than 3")
        exit(-1)

print("one:  " + str(one_step_count))
print("two:  " + str(two_step_count))
print("three:  " + str(three_step_count))

print("one x three = " + str(one_step_count*three_step_count))