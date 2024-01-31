import sys
N = int(input())
num_list = []
num_dict = {}
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    num_list.append(num)
    if num_dict.get(num) == None:
        num_dict[num] = 1
    else:
        num_dict[num] += 1

num_list.sort()
sorted_count = sorted(num_dict.items(), key = lambda x : (-x[1], x[0]))

# print(num_list)
# print(sorted_count)

print(round(sum(num_list)/N))
print(num_list[N // 2])
if len(num_list) == 1:
    print(num_list[0])
else:
    if sorted_count[0][1] != sorted_count[1][1]:
        print(sorted_count[0][0])
    else:
        print(sorted_count[1][0])
print(max(num_list) - min(num_list))
