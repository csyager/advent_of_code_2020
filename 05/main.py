import math

with open('chase_input.txt') as f:
    input_file = f.readlines()
input_file = [x.strip() for x in input_file]

highest_id = 0

id_array = []

seat_array = []
for i in range(0, 128):
    row = []
    for j in range(0, 8):
        row.append(" ")
    seat_array.append(row)

for elem in input_file:
    upper = 127
    lower = 0
    for c in range(0, 7):
        if elem[c] == "F":
            upper = math.floor((upper+lower)/2)
        if elem[c] == "B":
            lower = math.ceil((upper+lower)/2)
    
    upper_col = 7
    lower_col = 0

    for e in range(7, 10):
        if elem[e] == "L":
            upper_col = math.floor((upper_col+lower_col)/2)
        if elem[e] == "R":
            lower_col = math.ceil((upper_col+lower_col)/2)
        
    if upper != lower or upper_col != lower_col:
        print("Error:  values are not equal")
        print(elem)
        print("Upper: " + str(upper))
        print("Lower: " + str(lower))
        print("Upper col: " + str(upper_col))
        print("Lower col: " + str(lower_col))
    
    seat_array[upper][upper_col] = "X"
    id = upper * 8 + upper_col
    id_array.append(id)
    if (id > highest_id):
        highest_id = id

for row in range(0, len(seat_array)):
    for col in range(0, len(seat_array[row])):
        if seat_array[row][col] != "X":
            id = row * 8 + col
            if id + 1 in id_array and id - 1 in id_array:
                print(id)

print("highest " + str(highest_id))