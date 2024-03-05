# 2 x n 타일링 2

dp = [0] * 1001
dp[1] = 1
dp[2] = 3

n = int(input())

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007

print(dp[n])