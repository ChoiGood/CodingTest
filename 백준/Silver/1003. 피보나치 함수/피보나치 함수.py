import sys
input = sys.stdin.readline

dp = [0] * 100
dp[0] = (1, 0)
dp[1] = (0, 1)

for i in range(2, 100):
    a = dp[i - 1][0] + dp[i - 2][0]
    b = dp[i - 1][1] + dp[i - 2][1]
    dp[i] = (a, b)

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    print(*dp[N])