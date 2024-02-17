# 어려운 소인수분해
# DP + 역추적

# N : 1,000,000
# 2 <= k <= 5,000,000 이 N 개 주어진다

# 에라토스테네스의 체 
dp = [0] * 5000001 # 소수 판정
path = [0] * 5000001 # 역추적을 위한 path
for i in range(2, 5000001):
    dp[i] = i
    path[i] = i

for i in range(2, 5000001):
    if dp[i] == 0:
        continue
    for j in range(i*i, 5000001, i):
        dp[j] = 0
        if path[j] > i:
            path[j] = i # 역추적을 위한 작업

N = int(input())
numbers = list(map(int, input().split()))

for num in numbers:
    while num != 1:
        print(path[num], end = ' ')
        num //= path[num]
    print()