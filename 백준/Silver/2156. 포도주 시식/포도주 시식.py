# 포도주 시식
import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [0]
for _ in range(N):
    tmp = int(input().rstrip())
    arr.append(tmp)

dp = [0] * (10000 + 1)

if N == 1:
    dp[1] = arr[1]
if N == 2:
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]

if N >= 3:
    dp[1], dp[2] = arr[1], arr[1] + arr[2]
    dp[3] = max(arr[2] + arr[3], arr[1] + arr[3])
    for i in range(4, N + 1):
        dp[i] = max(dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i], dp[i - 4] + arr[i - 1] + arr[i])

print(max(dp)) 
