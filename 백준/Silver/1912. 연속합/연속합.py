# 연속합

# 1. 누적합, 이중 for 문 ==> 시간초과
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
S = [0] * (n + 1)

for i in range(1, n + 1):
    S[i] = S[i - 1] + arr[i]

t_max = S[1]
t_min = S[1]
for i in range(2, n + 1):
    if t_max < max(S[i], S[i] - t_min):
        t_max = max(S[i], S[i] - t_min)
    
    if t_min > S[i]:
        t_min = S[i]

print(t_max)
    




# 이중 for 문 ==> 시간초과
# t_max = -10000000000
# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         tmp = S[j] - S[i - 1]
#         if t_max < tmp:
#             t_max = tmp
# print(t_max)


