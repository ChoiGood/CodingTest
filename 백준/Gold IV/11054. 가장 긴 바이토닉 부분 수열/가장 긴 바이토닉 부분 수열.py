# 가장 긴 바이토닉 부분 수열
n = int(input()) # 1 <= N <= 1000
arr = list(map(int, input().split()))

dp1 = [0] * n # 왼쪽부터 만들어지는 LIS (최장 증가 부분 수열)
dp2 = [0] * n # 오른쪽부터 만들어지는 LIS (최장 증가 부분 수열)
dp3 = [0] * n # 바이토닉 수열

for i in range(n):
    dp1[i] = 1
    for j in range(i):
        if arr[j] < arr[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

for i in range(n - 1, -1, -1):
    dp2[i] = 1
    for j in range(n - 1, i, -1):
        if arr[j] < arr[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

for i in range(n):
    dp3[i] = dp1[i] + dp2[i] - 1

print(max(dp3))

