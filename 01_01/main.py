import time
start_time = time.time()

with open('input.txt') as f:
    input = f.readlines()
input = [x.strip() for x in input]

for i in input:
    for j in input:
        if int(i)+int(j) == 2020:
            print(i, j)

print(time.time() - start_time)
            