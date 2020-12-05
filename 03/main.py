with open('input.txt') as f:
    input_file = f.readlines()
input_file = [x.strip() for x in input_file]

possible_slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

tree_counts = []

for pair in possible_slopes:
    current_x = 0
    current_y = 0
    x_slope = pair[0]
    y_slope = pair[1]
    tree_count = 0

    while current_y < len(input_file):
        try:
            if input_file[current_y][current_x] == "#":
                tree_count += 1
        except IndexError as e:
            print(e)
            print(str(current_x) + " " + str(current_y))
            exit(-1)
        current_x += x_slope
        current_x %= 31
        current_y += y_slope
    
    tree_counts.append(tree_count)

print(tree_counts)
product = 1
for c in tree_counts:
    product = product * c

print(product)


# current_x = 0
# tree_count = 0
# for i in range(0, len(input_file)):
#     if input_file[i][current_x] == "#":
#         tree_count += 1
    
#     current_x += 3
#     current_x %= 31

