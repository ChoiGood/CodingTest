N = int(input())

dp = [0] * (1000000 + 1)

dp[2], dp[3] = 1, 1

for i in range(4, N + 1):
    if i % 2 == 0 and i % 3 == 0:
        dp[i] = 1 + min(dp[i // 2], dp[i // 3], dp[i - 1])
    elif i % 2 == 0:
        dp[i] = 1 + min(dp[i // 2], dp[i - 1])
    elif i % 3 == 0:
        dp[i] = 1 + min(dp[i // 3], dp[i - 1])
    else:
        dp[i] = 1 + dp[i - 1]

print(dp[N])