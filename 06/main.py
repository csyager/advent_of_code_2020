with open('input.txt') as f:
    input_file = f.readlines()
input_file = [x.rstrip() for x in input_file]

# input_file = [
#     "fukpz",
#     "ojqxynz",
#     "bkrz",
#     "rmspz"
# ]

input_file.append("")

total_sum = 0
partial_sum = 0
next_is_first = True
partial_answers = []

for elem in input_file:
    if elem == "":
        partial_sum = len(partial_answers)
        print(partial_answers)
        print(partial_sum)
        total_sum += partial_sum
        partial_sum = 0
        partial_answers = []
        next_is_first = True
    else:
        print(elem)
        if next_is_first:
            for c in elem:
                partial_answers.append(c)
            next_is_first = False
        else:
            partial_answers_copy = []
            for ans in partial_answers:
                partial_answers_copy.append(ans)
            for c in partial_answers:
                if c not in elem:
                    partial_answers_copy.remove(c)
            partial_answers = partial_answers_copy

print(total_sum)