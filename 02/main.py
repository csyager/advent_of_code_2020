with open('input.txt') as f:
    input_file = f.readlines()
input_file = [x.strip() for x in input_file]

count = 0

for i in range(0, len(input_file)):
    input_arr = input_file[i].split()
    position1 = int(input_arr[0].split('-')[0])
    position2 = int(input_arr[0].split('-')[1])
    password = input_arr[2]
    character = input_arr[1][:1]
    
    if (password[position1 - 1]==character) ^ (password[position2 - 1]==character):
        count += 1
    else:
        print(str(position1) + ", " + str(position2) + " " + character + " " + password)

print(count)