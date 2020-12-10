with open('test_input.txt') as f:
    input_file = f.readlines()
input_file = [x.rstrip() for x in input_file]
input_file = list(map(int, input_file))
input_file.append(0)
input_file.sort()

recalculations = [0] * len(input_file)

def find_arrangements(adapter_list):
    # "depth", or what part of the array is being calculated currently
    depth = len(input_file) - len(adapter_list)
    recalculations[depth] += 1
    # base case
    if len(adapter_list) == 1:
        return 1
    
    # check possible paths.  return the sum of these paths
    else:
        sum = 0
        if adapter_list[1] - adapter_list[0] <= 3:
            sum += find_arrangements(adapter_list[1:])

        # in case the list is too short
        try:
            if adapter_list[2] - adapter_list[0] <= 3:
                sum += find_arrangements(adapter_list[2:])
        except IndexError:
            pass

        try:
            if adapter_list[3] - adapter_list[0] <= 3:
                sum += find_arrangements(adapter_list[3:])
        except IndexError:
            pass
        
        return sum

print(find_arrangements(input_file))
print(recalculations)