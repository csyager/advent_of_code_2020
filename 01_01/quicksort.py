import time
start_time = time.time()

with open('input.txt') as f:
    input_arr = f.readlines()
input_arr = [x.strip() for x in input_arr]
input_arr = [int(x) for x in input_arr]


def quicksort(arr, left_index, right_index):
    if len(arr) == 1:
        return arr
    
    if left_index < right_index:
        partition_index = partition(arr, left_index, right_index)
        quicksort(arr, left_index, partition_index-1)
        quicksort(arr, partition_index+1, right_index)

def partition(arr, left_index, right_index):
    pivot = arr[right_index]

    i = left_index -1
    j = right_index - 1
    for j in range(left_index, right_index):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[right_index] = arr[right_index], arr[i+1]
    return i+1

quicksort(input_arr, 0, len(input_arr)-1)

left_pointer = 0
right_pointer = len(input_arr)-1

target_sum = 2020
while(input_arr[left_pointer] + input_arr[right_pointer] != target_sum):
    if input_arr[left_pointer] + input_arr[right_pointer] < target_sum:
        left_pointer += 1
    if input_arr[left_pointer] + input_arr[right_pointer] > target_sum:
        right_pointer -= 1

print(input_arr[left_pointer], input_arr[right_pointer])
print(time.time()-start_time)