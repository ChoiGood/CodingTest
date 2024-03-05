# 동전 1
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins_value = [0]
for _ in range(n):
    coins_value.append(int(input().rstrip()))


# dp = [[0] * (k + 1) for _ in range(n + 1)]
# for i in range(1, n + 1):
#     dp[i][0] = 1

# for i in range(1, n + 1):
#     for j in range(1, coins_value[i]):
#         dp[i][j] = dp[i - 1][j]
    
#     for j in range(coins_value[i], k + 1):
#         dp[i][j] = dp[i - 1][j] + dp[i][j - coins_value[i]]
# => 메모리 제한이 4 MB 이므로 메모리 초과 발생!! => 이차원 dp를 일차원으로 줄여보자!!


dp = [0] * (k + 1)
dp[0] = 1
for i in range(1,  n + 1):
    for j in range(coins_value[i], k + 1):
        dp[j] += dp[j - coins_value[i]]

print(dp[k])