# 가장 긴 증가하는 부분 수열
N = int(input())
arr = list(map(int, input().split()))

# dp[i] : 해당 index에서 가장 긴 부분 수열의 길이 뜻함!!
dp = [0] * N

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))