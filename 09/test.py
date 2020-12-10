with open('test.txt') as f:
    input_file = f.readlines()
input_file = [x.rstrip() for x in input_file]

def possible_sum_exists(index):
    value = int(input_file[index])
    for i in range(1, 6):
        for j in range(1, 6):
            if i != j:
                if int(input_file[index-i]) + int(input_file[index-j]) == value:
                    return True
    return False

for elem_index in range(5, len(input_file)):
    if not possible_sum_exists(elem_index):
        target = int(input_file[elem_index])
        print(target)


for starting_index in range(0, len(input_file)):
    for ending_index in range(starting_index+1, len(input_file)):
        sum = 0
        for index in range(starting_index, ending_index+1):
            sum += int(input_file[index])
        if sum == target:
            print(sum)
            print("starting_index: " + str(starting_index))
            print("ending index: " + str(ending_index))
            min = int(input_file[starting_index])
            max = int(input_file[ending_index])
            for e in range(starting_index, ending_index+1):
                if int(input_file[e]) < min:
                    min = int(input_file[e])
                if int(input_file[e]) > max:   
                    max = int(input_file[e])
            print('min/max sum: ' + str(min + max))
    
    