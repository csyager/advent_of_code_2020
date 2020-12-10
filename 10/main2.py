with open('input.txt') as f:
    input_file = f.readlines()
input_file = [x.rstrip() for x in input_file]
input_file = list(map(int, input_file))
input_file.append(0)
input_file.sort()
input_file.append(input_file[len(input_file)-1] + 3)

print(input_file)

dp = [0] * len(input_file)
dp[0] = 1

for i in range(1, len(input_file)):
    j = i-1
    while input_file[i] - input_file[j] <= 3 and j >= 0: 
        dp[i] += dp[j]
        j-=1
    
print(dp)


# def find_arrangements(adapter_list):
#     # base case
#     if len(adapter_list) == 1:
#         return 1
    
#     # check possible paths.  return the sum of these paths
#     else:
#         sum = 0
#         if adapter_list[1] - adapter_list[0] <= 3:
#             sum += find_arrangements(adapter_list[1:])

#         # in case the list is too short
#         try:
#             if adapter_list[2] - adapter_list[0] <= 3:
#                 sum += find_arrangements(adapter_list[2:])
#         except IndexError:
#             pass

#         try:
#             if adapter_list[3] - adapter_list[0] <= 3:
#                 sum += find_arrangements(adapter_list[3:])
#         except IndexError:
#             pass
        
#         return sum

# print(find_arrangements(input_file))